from typing import Optional

from aiokit import AioThing
from psycopg.rows import tuple_row
from psycopg_pool import AsyncConnectionPool


class AioPostgresPoolHolder(AioThing):
    def __init__(self, conninfo, timeout=30, min_size=1, max_size=4):
        super().__init__()
        self.pool = None
        self.fn = lambda: AsyncConnectionPool(
            conninfo=conninfo,
            timeout=timeout,
            min_size=min_size,
            max_size=max_size,
        )

    async def start(self):
        if not self.pool:
            self.pool = self.fn()

    async def stop(self):
        if self.pool:
            await self.pool.close()
            self.pool = None

    async def iterate(
        self,
        stmt: str,
        values=None,
        row_factory=tuple_row,
        cursor_name: Optional[str] = None,
        itersize: Optional[int] = None,
    ):
        if not self.pool:
            raise RuntimeError('AioPostgresPoolHolder has not been started')
        async with self.pool.connection() as conn:
            async with conn.cursor(name=cursor_name, row_factory=row_factory) as cur:
                if itersize is not None:
                    cur.itersize = itersize
                await cur.execute(stmt, values)
                async for row in cur:
                    yield row

    async def execute(self, stmt: str, values=None, cursor_name: Optional[str] = None, row_factory=tuple_row):
        if not self.pool:
            raise RuntimeError('AioPostgresPoolHolder has not been started')
        async with self.pool.connection() as conn:
            async with conn.cursor(name=cursor_name, row_factory=row_factory) as cur:
                await cur.execute(stmt, values)
