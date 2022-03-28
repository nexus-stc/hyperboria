import re
from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log

from .base import (
    Md5Source,
    PreparedRequest,
)


class LibgenMd5Source(Md5Source):
    base_url = 'http://libgen.rocks'
    resolve_timeout = 10

    async def resolve_lg(self, session, url):
        async with PreparedRequest(
            method='get',
            url=url,
            timeout=self.resolve_timeout
        ).execute_with(session=session) as resp:
            downloaded_page = await resp.text()
        match = re.search(
            'get\\.php\\?md5=.*&key=[A-Za-z0-9]+',
            downloaded_page,
            re.IGNORECASE,
        )
        if match:
            return PreparedRequest(method='get', url=f'{self.base_url}/{match.group()}', timeout=self.timeout)

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/ads.php?md5={self.md5}'
            result = await self.resolve_lg(session, url)
            if result:
                yield result
            url = f'{self.base_url}/foreignfiction/ads.php?md5={self.md5}'
            result = await self.resolve_lg(session, url)
            if result:
                yield result
