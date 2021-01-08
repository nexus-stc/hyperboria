from typing import AsyncIterable

from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class BiorxivSource(DoiSource):
    base_url = 'https://dx.doi.org'

    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/{self.doi}'
            async with session.get(
                url,
                timeout=self.resolve_timeout
            ) as resp:
                yield PreparedRequest(method='get', url=str(resp.url) + '.full.pdf')
