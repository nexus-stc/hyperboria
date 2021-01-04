from typing import (
    Any,
    AsyncIterable,
    Iterable,
)

import aiopg
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.ingest.jobs.base import BaseJob


class SelfFeedJob(BaseJob):
    name = 'self-feed-job'

    def __init__(
        self,
        database: dict,
        sql: str,
        actions: Iterable[dict],
        sinks: Iterable[dict],
    ):
        super().__init__(actions=actions, sinks=sinks)
        self.sql = sql
        self.pool_holder = AioPostgresPoolHolder(
            fn=aiopg.create_pool,
            dsn=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
            timeout=30,
            pool_recycle=60,
            maxsize=4,
        )
        self.waits.append(self.pool_holder)

    async def iterator(self) -> AsyncIterable[Any]:
        rows = await self.pool_holder.execute(self.sql, fetch=True, timeout=3600)
        for row in rows:
            yield row
