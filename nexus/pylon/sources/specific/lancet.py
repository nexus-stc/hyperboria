from typing import AsyncIterable

from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class LancetSource(DoiSource):
    base_url = 'https://www.thelancet.com'
    resolve_timeout = 10
    use_proxy = False

    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            splitted_doi = self.doi.split("/", maxsplit=1)
            if len(splitted_doi) < 2:
                return
            url = f'{self.base_url}/action/showPdf?pii={splitted_doi[1].upper()}'
            async with session.get(
                url,
                timeout=self.resolve_timeout
            ) as resp:
                yield PreparedRequest(method='get', cookies=resp.cookies, url=str(resp.url))
