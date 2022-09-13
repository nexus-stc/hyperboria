import logging
from typing import (
    AsyncIterable,
    Dict,
)

from aiokit import AioThing
from nexus.pylon.exceptions import (
    DownloadError,
    NotFoundError,
)
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.pylon.proxy_manager import ProxyManager
from nexus.pylon.source import Source


class PylonClient(AioThing):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.proxy_manager = ProxyManager(config.get('proxies'))
        self.sources = []
        if config.get('webdriver_hub') is None:
            logging.getLogger('nexus_pylon').warning({
                'action': 'missed_webdriver',
                'mode': 'pylon',
            })
        for source_config in config['sources']:
            source = Source.from_config(
                proxy_manager=self.proxy_manager,
                config=self.config,
                source_config=source_config,
            )
            if source:
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
            except NotFoundError as e:
                logging.getLogger('nexus_pylon').debug(e)
                continue
            except DownloadError as e:
                logging.getLogger('nexus_pylon').warning(e)
                continue
        raise NotFoundError(params=params)
