from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class NejmSource(DoiSource):
    base_url = 'https://www.nejm.org'
    resolve_timeout = 10
    use_proxy = False

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/doi/pdf/{self.doi}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp:
                yield PreparedRequest(method='get', cookies=resp.cookies, url=str(resp.url), timeout=self.timeout)
