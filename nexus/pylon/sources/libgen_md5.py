import re
from typing import AsyncIterable

from .base import (
    Md5Source,
    PreparedRequest,
)


class LibgenMd5Source(Md5Source):
    base_url = 'http://libgen.gs'
    resolve_timeout = 10

    async def resolve_lg(self, session, url):
        async with session.get(
            url,
            timeout=self.resolve_timeout
        ) as resp:
            downloaded_page_fiction = await resp.text()
        match = re.search(
            'https?://.*/get\\.php\\?md5=.*&key=[A-Za-z0-9]+',
            downloaded_page_fiction,
            re.IGNORECASE,
        )
        if match:
            return PreparedRequest(method='get', url=match.group())

    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/ads.php?md5={self.md5}'
            result = await self.resolve_lg(session, url)
            if result:
                yield result
            url = f'{self.base_url}/foreignfiction/ads.php?md5={self.md5}'
            result = await self.resolve_lg(session, url)
            if result:
                yield result
