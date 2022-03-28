from datetime import (
    datetime,
    timedelta,
)
from typing import (
    Any,
    AsyncIterable,
    Iterable,
    Optional,
)

from aiolibgen import LibgenClient
from nexus.ingest.jobs.base import BaseJob


class LibgenApiJob(BaseJob):
    name = 'libgen-api'

    def __init__(
        self,
        base_url: str,
        max_retries: int,
        retry_delay: int,
        actions: Iterable[dict],
        sinks: Iterable[dict],
        from_date: Optional[str] = None,
    ):
        super().__init__(sinks=sinks, actions=actions)
        self.libgen_client = LibgenClient(base_url=base_url, max_retries=max_retries, retry_delay=retry_delay)
        self.from_date = from_date or str(datetime.date(datetime.now()) - timedelta(days=1))
        self.waits.append(self.libgen_client)

    async def iterator(self) -> AsyncIterable[Any]:
        async for item in self.libgen_client.newer(timenewer=f'{self.from_date} 00:00:00'):
            yield item
