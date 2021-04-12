import re
from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.exceptions import RegexNotFoundError

from .base import (
    DoiSource,
    PreparedRequest,
)


class LibgenDoiSource(DoiSource):
    base_url = 'http://libgen.gs'
    resolve_timeout = 10

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/scimag/ads.php?doi={self.doi}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp:
                downloaded_page_bytes = await resp.read()
                downloaded_page = downloaded_page_bytes.decode('utf-8', 'backslashreplace')
            match = re.search(
                'https?://.*/scimag/get\\.php\\?doi=.*&key=[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match:
                yield PreparedRequest(method='get', url=match.group(), timeout=self.timeout)
            else:
                error_log_func(RegexNotFoundError(url=url))
