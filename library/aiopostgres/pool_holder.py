import asyncio
import logging
from typing import Optional

import psycopg
from aiokit import AioThing
from izihawa_utils.exceptions import BaseError
from psycopg.rows import tuple_row
from psycopg_pool import AsyncConnectionPool


class OperationalError(BaseError):
    level = logging.WARNING
    code = 'operational_error'


class AioPostgresPoolHolder(AioThing):
    def __init__(self, conninfo, timeout=30, min_size=1, max_size=1, is_recycling=True):
        super().__init__()
        self.pool = None
        self.fn = lambda: AsyncConnectionPool(
            conninfo=conninfo,
            timeout=timeout,
            min_size=min_size,
            max_size=max_size + int(is_recycling),
        )
        self.is_recycling = is_recycling
        self.recycling_task = None
        self.timeout = timeout

    async def _get_connection(self):
        ev = asyncio.Event()
        conn = await self.pool.getconn()
        asyncio.get_running_loop().add_reader(conn.fileno(), ev.set)
        return ev, conn

    async def recycling(self):
        logging.getLogger('debug').debug({
            'action': 'start_recycling',
            'mode': 'pool',
            'stats': self.pool.get_stats(),
        })
        ev, conn = await self._get_connection()
        try:
            while True:
                try:
                    await asyncio.wait_for(ev.wait(), self.timeout)
                except asyncio.TimeoutError:
                    continue
                try:
                    await conn.execute("SELECT 1")
                except psycopg.OperationalError:
                    asyncio.get_running_loop().remove_reader(conn.fileno())
                    await self.pool.putconn(conn)
                    await self.pool.check()
                    ev, conn = await self._get_connection()
        except asyncio.CancelledError:
            pass
        finally:
            await self.pool.putconn(conn)
            logging.getLogger('debug').debug({
                'action': 'stopped_recycling',
                'mode': 'pool',
                'stats': self.pool.get_stats(),
            })

    async def start(self):
        if not self.pool:
            self.pool = self.fn()
            await self.pool.wait()
            if self.is_recycling:
                self.recycling_task = asyncio.create_task(self.recycling())

    async def stop(self):
        if self.pool:
            if self.recycling_task:
                self.recycling_task.cancel()
                await self.recycling_task
                self.recycling_task = None
            logging.getLogger('debug').debug({
                'action': 'close',
                'mode': 'pool',
                'stats': self.pool.get_stats(),
            })
            await self.pool.close()
            self.pool = None

    async def iterate(
        self,
        stmt: str,
        values=None,
        row_factory=tuple_row,
        cursor_name: Optional[str] = None,
        itersize: Optional[int] = None,
        statement_timeout: Optional[int] = None,
    ):
        if not self.pool:
            raise RuntimeError('AioPostgresPoolHolder has not been started')
        async with self.pool.connection() as conn:
            async with conn.cursor(name=cursor_name, row_factory=row_factory) as cur:
                if itersize is not None:
                    cur.itersize = itersize
                await cur.execute(stmt + ';' if statement_timeout else '', values)
                if statement_timeout:
                    await cur.execute(f'SET statement_timeout = {statement_timeout};')
                async for row in cur:
                    yield row

    async def execute(self, stmt: str, values=None, cursor_name: Optional[str] = None, row_factory=tuple_row):
        if not self.pool:
            raise RuntimeError('AioPostgresPoolHolder has not been started')
        async with self.pool.connection() as conn:
            async with conn.cursor(name=cursor_name, row_factory=row_factory) as cur:
                await cur.execute(stmt, values)
