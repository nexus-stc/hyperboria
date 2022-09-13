from typing import (
    AsyncIterable,
    List,
    Optional,
)

from nexus.pylon.prepared_request import PreparedRequest
from nexus.pylon.proxy_manager import ProxyManager
from nexus.pylon.resolvers.base import BaseResolver


class TemplateResolver(BaseResolver):
    def __init__(
        self,
        format_string: str = 'https://doi.org/{doi}',
        timeout: float = 10.0,
        method: str = 'GET',
        headers: Optional[dict] = None,
        headers_override: bool = False,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        super().__init__(proxy_list=proxy_list, proxy_manager=proxy_manager)
        self.format_string = format_string
        self.timeout = timeout
        self.method = method
        self.headers = headers
        self.headers_override = headers_override

    def __str__(self):
        return f'{self.__class__.__name__}({self.format_string})'

    async def resolve(self, params) -> AsyncIterable[PreparedRequest]:
        yield PreparedRequest(
            method=self.method,
            url=self.format_string.format(**params),
            timeout=self.timeout,
            headers=self.headers,
            headers_override=self.headers_override,
        )
