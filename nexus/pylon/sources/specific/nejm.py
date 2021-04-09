from typing import AsyncIterable

from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class NejmSource(DoiSource):
    base_url = 'https://www.nejm.org'
    resolve_timeout = 10
    use_proxy = False

    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/doi/pdf/{self.doi}'
            async with session.get(
                url,
                timeout=self.resolve_timeout,
            ) as resp:
                yield PreparedRequest(method='get', cookies=resp.cookies, url=str(resp.url))
