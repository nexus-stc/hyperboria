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


class ResearchSquareSource(DoiSource):
    base_url = 'https://dx.doi.org'

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/{self.doi}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp:
                download_page = await resp.text()
            match = re.search(
                r'\"(https://www\.researchsquare\.com/article/[^\"]+\.pdf)\"',
                download_page,
                re.IGNORECASE,
            )
            if not match:
                raise RegexNotFoundError(url=url)
            yield PreparedRequest(method='get', url=match.group(1), timeout=self.timeout)
