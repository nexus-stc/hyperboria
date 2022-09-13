import asyncio
import logging
from contextlib import asynccontextmanager
from typing import Optional

import aiohttp
import aiohttp.client_exceptions
from aiohttp import ClientTimeout
from aiohttp_socks import ProxyConnectionError
from nexus.pylon.consts import DEFAULT_USER_AGENT
from nexus.pylon.exceptions import (
    BadResponseError,
    DownloadError,
)


class PreparedRequest:
    def __init__(
        self,
        method: str,
        url: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        cookies: Optional[dict] = None,
        ssl: bool = True,
        timeout: Optional[float] = None,
        headers_override: bool = False
    ):
        self.method = method
        self.url = url
        self.headers = {
            'Connection': 'keep-alive',
            'User-Agent': DEFAULT_USER_AGENT,
        }
        if headers:
            self.headers.update(headers)
        if headers_override:
            self.headers = headers or {}
        self.params = params
        self.cookies = cookies
        self.ssl = ssl
        self.timeout = timeout

    def __repr__(self):
        r = f'{self.method} {self.url} {self.headers}'
        if self.params:
            r += f' {self.params}'
        return r

    def __str__(self):
        return repr(self)

    @asynccontextmanager
    async def execute_with(self, session):
        try:
            logging.getLogger('nexus_pylon').debug({
                'action': 'request',
                'mode': 'pylon',
                'url': self.url,
                'method': self.method,
                'headers': self.headers,
            })
            async with session.request(
                method=self.method,
                url=self.url,
                timeout=ClientTimeout(
                    sock_read=self.timeout,
                ),
                headers=self.headers,
                cookies=self.cookies,
                params=self.params,
                ssl=self.ssl,
            ) as resp:
                yield resp
        except BadResponseError as e:
            e.add('url', self.url)
            raise e
        except (
            aiohttp.client_exceptions.ClientConnectionError,
            aiohttp.client_exceptions.ClientResponseError,
            aiohttp.client_exceptions.InvalidURL,
            aiohttp.client_exceptions.TooManyRedirects,
            asyncio.exceptions.IncompleteReadError,
            asyncio.TimeoutError,
            ConnectionAbortedError,
            ConnectionResetError,
            ProxyConnectionError,
        ) as e:
            raise DownloadError(
                nested_error=repr(e),
                url=self.url,
            )
