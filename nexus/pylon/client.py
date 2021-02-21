import asyncio
from typing import (
    AsyncIterable,
    Iterable,
    Optional,
)

import aiohttp
import aiohttp.client_exceptions
from aiohttp_socks import (
    ProxyConnectionError,
    ProxyError,
)
from aiokit import AioThing
from library.logging import error_log
from nexus.pylon.exceptions import (
    DownloadError,
    NotFoundError,
)
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.pylon.sources import (
    BaseSource,
    LibgenDoiSource,
    LibgenMd5Source,
    LibraryLolSource,
    SciHubDoSource,
    SciHubSeSource,
)
from nexus.pylon.sources.specific import get_specific_sources_for_doi
from python_socks import ProxyTimeoutError


class PylonClient(AioThing):
    def __init__(self, proxy: Optional[str] = None, resolve_proxy: Optional[str] = None):
        super().__init__()
        self.proxy = proxy
        self.resolve_proxy = resolve_proxy

    async def by_doi(
        self,
        doi: str,
        md5: Optional[str] = None,
    ) -> AsyncIterable[FileResponsePb]:
        sources = []
        sources.extend(get_specific_sources_for_doi(doi, proxy=self.proxy, resolve_proxy=self.resolve_proxy))
        sources.extend([
            SciHubDoSource(doi=doi, md5=md5, proxy=self.proxy, resolve_proxy=self.resolve_proxy),
            SciHubSeSource(doi=doi, md5=md5, proxy=self.proxy, resolve_proxy=self.resolve_proxy),
            LibgenDoiSource(doi=doi, md5=md5, proxy=self.proxy, resolve_proxy=self.resolve_proxy),
        ])
        sources = filter(lambda x: x.is_enabled, sources)
        async for resp in self.download(sources=sources):
            yield resp

    async def by_md5(
        self,
        md5: str,
    ) -> AsyncIterable[FileResponsePb]:
        sources = filter(lambda x: x.is_enabled, [
            LibraryLolSource(md5=md5, proxy=self.proxy, resolve_proxy=self.resolve_proxy),
            LibgenMd5Source(md5=md5, proxy=self.proxy, resolve_proxy=self.resolve_proxy),
        ])
        async for resp in self.download(sources=sources):
            yield resp

    async def download_source(self, source) -> AsyncIterable[FileResponsePb]:
        try:
            yield FileResponsePb(status=FileResponsePb.Status.RESOLVING, source=source.base_url)
            async for prepared_request in source.resolve():
                async for resp in source.execute_prepared_request(prepared_request=prepared_request):
                    yield resp
                return
            raise DownloadError(error='not_found', source=str(source))
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
            raise DownloadError(nested_error=str(e), nested_error_cls=e.__class__.__name__)

    async def download(self, sources: Iterable[BaseSource]) -> AsyncIterable[FileResponsePb]:
        for source in sources:
            try:
                await source.start()
                async for resp in self.download_source(source):
                    yield resp
                return
            except DownloadError as e:
                error_log(e)
                continue
            finally:
                await source.stop()
        raise NotFoundError()
