from typing import (
    AsyncIterable,
    Dict,
    List,
    Optional,
)

from aiokit import AioThing
from library.logging import error_log
from nexus.pylon.exceptions import (
    DownloadError,
    NotFoundError,
)
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.pylon.proxy_manager import ProxyManager
from nexus.pylon.source import Source


class PylonClient(AioThing):
    def __init__(
        self,
        source_configs: Optional[List],
        proxies: Optional[List[str]] = None,
        downloads_directory: Optional[str] = None,
        default_driver_proxy_list: [Optional[List]] = None,
        default_resolver_proxy_list: [Optional[List]] = None,
    ):
        super().__init__()
        self.proxy_manager = ProxyManager(proxies)
        self.downloads_directory = downloads_directory
        self.default_driver_proxy_list = default_driver_proxy_list
        self.default_resolver_proxy_list = default_resolver_proxy_list
        self.sources = []
        for source_config in source_configs:
            source = Source.from_config(
                proxy_manager=self.proxy_manager,
                source_config=source_config,
                downloads_directory=downloads_directory,
                default_driver_proxy_list=default_driver_proxy_list,
                default_resolver_proxy_list=default_resolver_proxy_list,
            )
            self.sources.append(source)
            self.starts.append(source)

    async def download(self, params: Dict) -> AsyncIterable[FileResponsePb]:
        for source in self.sources:
            if not source.is_match(params):
                continue
            try:
                async for resp in source.download(params):
                    yield resp
                return
            except NotFoundError:
                continue
            except DownloadError as e:
                error_log(e)
                continue
        raise NotFoundError()
