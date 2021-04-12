from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class LancetSource(DoiSource):
    base_url = 'https://www.thelancet.com'
    resolve_timeout = 10
    use_proxy = False

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            splitted_doi = self.doi.split("/", maxsplit=1)
            if len(splitted_doi) < 2:
                return
            url = f'{self.base_url}/action/showPdf?pii={splitted_doi[1].upper()}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp:
                yield PreparedRequest(
                    method='get',
                    cookies=resp.cookies,
                    url=str(resp.url),
                    timeout=self.resolve_timeout,
                )
