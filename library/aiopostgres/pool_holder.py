import aiopg
import psycopg2.extras
from aiokit import AioThing
from psycopg2 import OperationalError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)


class AioPostgresPoolHolder(AioThing):
    def __init__(self, fn=aiopg.create_pool, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.pool = None

    @retry(
        retry=retry_if_exception_type(OperationalError),
        stop=stop_after_attempt(3),
        wait=wait_fixed(1.0),
    )
    async def start(self):
        if not self.pool:
            self.pool = await self.fn(*self.args, **self.kwargs)

    async def stop(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            self.pool = None

    async def execute(self, stmt, values=None, fetch=False, timeout=None, cursor_factory=psycopg2.extras.DictCursor):
        async with self.pool.acquire() as conn:
            async with conn.cursor(cursor_factory=cursor_factory) as cur:
                await cur.execute(stmt, values, timeout=timeout)
                if fetch:
                    return await cur.fetchall()
                return cur.rowcount
