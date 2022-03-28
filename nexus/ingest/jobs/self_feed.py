from typing import (
    Any,
    AsyncIterable,
    Iterable,
)

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
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
        )
        self.waits.append(self.pool_holder)

    async def iterator(self) -> AsyncIterable[Any]:
        async for row in self.pool_holder.iterate(self.sql):
            yield row
