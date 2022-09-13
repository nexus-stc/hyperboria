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
        resolve_timeout: float = 10.0,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        super().__init__(proxy_list=proxy_list, proxy_manager=proxy_manager)
        self.resolve_timeout = resolve_timeout
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
                timeout=self.resolve_timeout,
            ).execute_with(session=session) as resp:
                # Sometimes hosts return file URL
                if resp.headers.get('Content-Type') == 'application/pdf':
                    yield PreparedRequest(method='get', url=url, timeout=10.0)
                downloaded_page_bytes = await resp.read()
                downloaded_page = downloaded_page_bytes.decode('utf-8', 'backslashreplace')

            for extractor in self.extractors:
                match = re.search(extractor['re'], downloaded_page, re.IGNORECASE)
                if match:
                    yield PreparedRequest(
                        method='get',
                        url=extractor['producer']['format_string'].format(
                            host=resp.real_url.host,
                            **match.groupdict()
                        ),
                        timeout=extractor['producer'].get('timeout', 10.0),
                    )
