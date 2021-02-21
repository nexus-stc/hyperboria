import hashlib
import random
from typing import (
    AsyncIterable,
    Optional,
)

import aiohttp
import aiohttp.client_exceptions
from aiohttp_socks import (
    ProxyConnector,
    ProxyError,
)
from aiokit import AioThing
from nexus.pylon.exceptions import (
    BadResponseError,
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


class PreparedRequest:
    def __init__(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        cookies: dict = None,
        ssl: bool = True,
    ):
        self.method = method
        self.url = url
        self.headers = {
            'User-Agent': DEFAULT_USER_AGENT,
        }
        if headers:
            self.headers.update(headers)
        self.params = params
        self.cookies = cookies
        self.ssl = ssl

    def __repr__(self):
        return f'{self.method} {self.url} {self.headers} {self.params}'

    def __str__(self):
        return repr(self)


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
        elif not is_pdf(self.file):
            raise BadResponseError(doi=self.doi, file=str(self.file[:1000]))


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
        return aiohttp.ClientSession(connector=self.get_proxy())

    def get_resolve_session(self):
        return aiohttp.ClientSession(connector=self.get_resolve_proxy())

    def resolve(self) -> AsyncIterable[PreparedRequest]:
        raise NotImplementedError("`resolve` for BaseSource is not implemented")

    def get_validator(self):
        return BaseValidator()

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((ProxyError, aiohttp.client_exceptions.ClientPayloadError, ProxyTimeoutError)),
    )
    async def execute_prepared_request(self, prepared_request: PreparedRequest):
        async with self.get_session() as session:
            async with session.request(
                method=prepared_request.method,
                url=prepared_request.url,
                timeout=self.timeout,
                headers=prepared_request.headers,
                cookies=prepared_request.cookies,
                params=prepared_request.params,
                ssl=prepared_request.ssl,
            ) as resp:
                if resp.status == 404:
                    raise NotFoundError(url=prepared_request.url)
                elif (
                    resp.status != 200
                    or (
                        self.allowed_content_type
                        and resp.headers.get('Content-Type', '').lower() not in self.allowed_content_type
                    )
                ):
                    raise BadResponseError(
                        request_headers=prepared_request.headers,
                        url=prepared_request.url,
                        status=resp.status,
                        headers=str(resp.headers),
                    )
                file_validator = self.get_validator()
                # Randomness is required due to annoying bug of when separators
                # (\r\n) are splitted to different chunks
                # https://github.com/aio-libs/aiohttp/issues/4677
                yield FileResponsePb(status=FileResponsePb.Status.BEGIN_TRANSMISSION, source=prepared_request.url)
                async for content in resp.content.iter_chunked(1024 * 100 + random.randint(-1024, 1024)):
                    file_validator.update(content)
                    yield FileResponsePb(chunk=ChunkPb(content=content), source=prepared_request.url)
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
