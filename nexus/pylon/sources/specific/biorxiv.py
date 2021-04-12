from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class BiorxivSource(DoiSource):
    base_url = 'https://dx.doi.org'

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/{self.doi}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp:
                yield PreparedRequest(method='get', url=str(resp.url) + '.full.pdf', timeout=self.timeout)
