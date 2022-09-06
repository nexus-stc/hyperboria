import re
from typing import (
    AsyncIterable,
    List,
    Optional,
)

from nexus.pylon.prepared_request import PreparedRequest
from nexus.pylon.proxy_manager import ProxyManager
from nexus.pylon.resolvers.base import BaseResolver


class RequestResolver(BaseResolver):
    def __init__(
        self,
        url: str,
        extractors: List,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        super().__init__(proxy_list=proxy_list, proxy_manager=proxy_manager)
        self.url = url
        self.extractors = extractors

    def __str__(self):
        return f'{self.__class__.__name__}({self.url})'

    async def resolve(self, params) -> AsyncIterable[PreparedRequest]:
        async with self.get_session() as session:
            url = self.url.format(**params)
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=10.0,
            ).execute_with(session=session) as resp:
                # Sometimes sci-hub returns file
                if resp.headers.get('Content-Type') == 'application/pdf':
                    yield PreparedRequest(method='get', url=url, timeout=10.0)
                downloaded_page_bytes = await resp.read()
                downloaded_page = downloaded_page_bytes.decode('utf-8', 'backslashreplace')

            for extractor in self.extractors:
                match = re.search(extractor['re'], downloaded_page, re.IGNORECASE)
                if match:
                    matched_group = match.group(extractor['producer']['group'])
                    yield PreparedRequest(
                        method='get',
                        url=extractor['producer']['format_string'].format(matched_group=matched_group),
                        timeout=extractor['producer'].get('timeout', 10.0),
                    )
