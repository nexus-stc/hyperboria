import asyncio
import hashlib
import socket
from contextlib import asynccontextmanager
from typing import (
    AsyncIterable,
    Callable,
    Optional,
)

import aiohttp
import aiohttp.client_exceptions
from aiohttp.client_reqrep import ClientRequest
from aiohttp_socks import (
    ProxyConnectionError,
    ProxyConnector,
    ProxyError,
)
from aiokit import AioThing
from izihawa_utils.importlib import class_fullname
from library.logging import error_log
from nexus.pylon.exceptions import (
    BadResponseError,
    DownloadError,
    IncorrectMD5Error,
    NotFoundError,
)
from nexus.pylon.pdftools import is_pdf
from nexus.pylon.proto.file_pb2 import Chunk as ChunkPb
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from python_socks import ProxyTimeoutError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
)

DEFAULT_USER_AGENT = 'PylonBot/1.0 (Linux x86_64) PylonBot/1.0.0'


class KeepAliveClientRequest(ClientRequest):
    async def send(self, conn):
        sock = conn.protocol.transport.get_extra_info("socket")
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 2)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)

        return await super().send(conn)


class PreparedRequest:
    def __init__(
        self,
        method: str,
        url: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        cookies: Optional[dict] = None,
        ssl: bool = True,
        timeout: Optional[float] = None
    ):
        self.method = method
        self.url = url
        self.headers = {
            'Connection': 'keep-alive',
            'User-Agent': DEFAULT_USER_AGENT,
        }
        if headers:
            self.headers.update(headers)
        self.params = params
        self.cookies = cookies
        self.ssl = ssl
        self.timeout = timeout

    def __repr__(self):
        return f'{self.method} {self.url} {self.headers} {self.params}'

    def __str__(self):
        return repr(self)

    @asynccontextmanager
    async def execute_with(self, session):
        try:
            async with session.request(
                method=self.method,
                url=self.url,
                timeout=self.timeout,
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
            aiohttp.client_exceptions.ClientPayloadError,
            aiohttp.client_exceptions.ClientResponseError,
            aiohttp.client_exceptions.TooManyRedirects,
            asyncio.TimeoutError,
            ProxyConnectionError,
            ProxyTimeoutError,
            ProxyError,
        ) as e:
            raise DownloadError(nested_error=repr(e), nested_error_cls=class_fullname(e))


class BaseValidator:
    def update(self, chunk: bytes):
        pass

    def validate(self):
        pass


class Md5Validator(BaseValidator):
    def __init__(self, md5: str):
        self.md5 = md5
        self.v = hashlib.md5()

    def update(self, chunk: bytes):
        self.v.update(chunk)

    def validate(self):
        digest = self.v.hexdigest()
        if self.md5.lower() != digest.lower():
            raise IncorrectMD5Error(requested_md5=self.md5, downloaded_md5=digest)


class DoiValidator(BaseValidator):
    def __init__(self, doi: str, md5: Optional[str] = None):
        self.doi = doi
        self.md5 = md5
        self.file = bytes()
        self.v = hashlib.md5()

    def update(self, chunk):
        self.file += chunk
        self.v.update(chunk)

    def validate(self):
        if self.md5 and self.md5.lower() == self.v.hexdigest().lower():
            return
        elif not is_pdf(f=self.file):
            raise BadResponseError(doi=self.doi, file=str(self.file[:100]))


class BaseSource(AioThing):
    allowed_content_type = None
    base_url = None
    is_enabled = True
    resolve_timeout = None
    ssl = True
    timeout = None
    use_proxy = None

    def __init__(self, proxy: str = None, resolve_proxy: str = None):
        super().__init__()
        self.proxy = proxy
        self.resolve_proxy = resolve_proxy

    def get_proxy(self):
        if self.proxy and self.use_proxy is not False:
            return ProxyConnector.from_url(self.proxy, verify_ssl=self.ssl)
        return aiohttp.TCPConnector(verify_ssl=self.ssl)

    def get_resolve_proxy(self):
        if self.resolve_proxy and self.use_proxy is not False:
            return ProxyConnector.from_url(self.resolve_proxy, verify_ssl=self.ssl)
        return aiohttp.TCPConnector(verify_ssl=self.ssl)

    def get_session(self):
        return aiohttp.ClientSession(request_class=KeepAliveClientRequest, connector=self.get_proxy())

    def get_resolve_session(self):
        return aiohttp.ClientSession(request_class=KeepAliveClientRequest, connector=self.get_resolve_proxy())

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        raise NotImplementedError("`resolve` for BaseSource is not implemented")

    def get_validator(self):
        return BaseValidator()

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((ProxyError, aiohttp.client_exceptions.ClientPayloadError, ProxyTimeoutError)),
    )
    async def execute_prepared_file_request(self, prepared_file_request: PreparedRequest):
        async with self.get_session() as session:
            async with prepared_file_request.execute_with(session=session) as resp:
                if resp.status == 404:
                    raise NotFoundError(url=prepared_file_request.url)
                elif (
                    resp.status != 200
                    or (
                        self.allowed_content_type
                        and resp.headers.get('Content-Type', '').lower() not in self.allowed_content_type
                    )
                ):
                    raise BadResponseError(
                        request_headers=prepared_file_request.headers,
                        url=prepared_file_request.url,
                        status=resp.status,
                        headers=str(resp.headers),
                    )
                file_validator = self.get_validator()
                yield FileResponsePb(status=FileResponsePb.Status.BEGIN_TRANSMISSION, source=prepared_file_request.url)
                async for content, _ in resp.content.iter_chunks():
                    file_validator.update(content)
                    yield FileResponsePb(chunk=ChunkPb(content=content), source=prepared_file_request.url)
                file_validator.validate()


class Md5Source(BaseSource):
    def __init__(
        self,
        md5: str,
        proxy: Optional[str] = None,
        resolve_proxy: Optional[str] = None,
    ):
        super().__init__(proxy=proxy, resolve_proxy=resolve_proxy)
        self.md5 = md5

    def get_validator(self):
        return Md5Validator(self.md5)


class DoiSource(BaseSource):
    def __init__(
        self,
        doi: str,
        md5: Optional[str] = None,
        proxy: Optional[str] = None,
        resolve_proxy: Optional[str] = None,
    ):
        super().__init__(proxy=proxy, resolve_proxy=resolve_proxy)
        self.doi = doi
        self.md5 = md5

    def get_validator(self):
        return DoiValidator(self.doi, md5=self.md5)
