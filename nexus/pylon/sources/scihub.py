import re
from typing import AsyncIterable

from library.logging import error_log
from nexus.pylon.exceptions import RegexNotFoundError

from .base import (
    DoiSource,
    PreparedRequest,
)


class SciHubSource(DoiSource):
    allowed_content_type = {
        'application/octet-stream',
        'application/pdf',
        'application/pdf;charset=utf-8',
    }
    base_url = None
    ssl = False

    async def resolve(self, timeout=None) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/{self.doi}'
            async with session.get(
                url,
                timeout=timeout or self.timeout
            ) as resp:
                # Sometimes sci-hub returns file
                if resp.headers.get('Content-Type') == 'application/pdf':
                    yield PreparedRequest(method='get', url=url)
                downloaded_page_bytes = await resp.read()
                downloaded_page = downloaded_page_bytes.decode('utf-8', 'backslashreplace')
            match = re.search('(?:https?:)?//.*\\?download=true', downloaded_page, re.IGNORECASE)
            if match:
                url = match.group()
                if url.startswith('//'):
                    url = 'http:' + url
                yield PreparedRequest(method='get', url=url)
            else:
                error_log(RegexNotFoundError(url=url))


class SciHubDoSource(SciHubSource):
    base_url = 'https://sci-hub.do'


class SciHubSeSource(SciHubSource):
    base_url = 'https://sci-hub.se'
