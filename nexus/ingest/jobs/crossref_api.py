import logging
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

from aiocrossref import CrossrefClient
from nexus.ingest.jobs.base import BaseJob


class CrossrefApiJob(BaseJob):
    name = 'crossref-api'

    def __init__(
        self,
        base_url: str,
        max_retries: int,
        retry_delay: int,
        actions: Iterable[dict],
        sinks: Iterable[dict],
        from_date: Optional[str] = None,
    ):
        super().__init__(actions=actions, sinks=sinks)
        self.crossref_client = CrossrefClient(base_url=base_url, max_retries=max_retries, retry_delay=retry_delay)
        self.from_date = from_date or str(datetime.date(datetime.now()) - timedelta(days=1))
        self.starts.append(self.crossref_client)

    async def iterator(self) -> AsyncIterable[Any]:
        logging.getLogger('statbox').info({
            'action': 'start',
            'mode': 'ingest',
            'target_date': self.from_date,
        })
        count = 0
        async for chunk in self.crossref_client.works_cursor(
            filter=f'from-index-date:{self.from_date}',
            rows=500,
        ):
            for item in chunk['items']:
                yield item
                count += 1
        logging.getLogger('statbox').info({
            'action': 'done',
            'mode': 'ingest',
            'items': count,
            'target_date': self.from_date,
        })