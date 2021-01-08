import re
from typing import AsyncIterable

from library.logging import error_log
from nexus.pylon.exceptions import RegexNotFoundError

from .base import (
    DoiSource,
    PreparedRequest,
)


class LibgenDoiSource(DoiSource):
    base_url = 'http://libgen.gs'
    resolve_timeout = 10

    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/scimag/ads.php?doi={self.doi}'
            async with session.get(
                url,
                timeout=self.resolve_timeout
            ) as resp:
                downloaded_page_bytes = await resp.read()
                downloaded_page = downloaded_page_bytes.decode('utf-8', 'backslashreplace')
            match = re.search(
                'https?://.*/scimag/get\\.php\\?doi=.*&key=[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match:
                yield PreparedRequest(method='get', url=match.group())
            else:
                error_log(RegexNotFoundError(url=url))
