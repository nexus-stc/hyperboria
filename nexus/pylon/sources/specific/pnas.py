import re
from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.exceptions import RegexNotFoundError
from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class PnasSource(DoiSource):
    base_url = 'https://www.pnas.org'
    resolve_timeout = 10
    use_proxy = False

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/lookup/doi/{self.doi}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp_1:
                async with PreparedRequest(
                    method='get',
                    cookies=resp_1.cookies,
                    url=str(resp_1.url),
                    timeout=self.resolve_timeout,
                ).execute_with(session=session) as resp_2:
                    download_page = await resp_2.text()
            match = re.search(
                r'\"(https://www\.pnas\.org/content/pnas/[^\"]+\.pdf)\"',
                download_page,
                re.IGNORECASE,
            )
            if not match:
                raise RegexNotFoundError(url=url)
            yield PreparedRequest(method='get', url=match.group(1), timeout=self.timeout)
