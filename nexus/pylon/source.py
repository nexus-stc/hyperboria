import logging
from typing import (
    AsyncIterable,
    Dict,
    Optional,
)

from aiohttp.client_exceptions import ClientPayloadError
from aiokit import AioThing
from izihawa_utils.importlib import import_object
from nexus.pylon.drivers.base import BaseDriver
from nexus.pylon.exceptions import (
    DownloadError,
    NotFoundError,
)
from nexus.pylon.matcher import Matcher
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.pylon.resolvers.base import BaseResolver


class Source(AioThing):
    def __init__(self, matcher: Matcher, resolver: BaseResolver, driver: BaseDriver):
        super().__init__()
        self.matcher = matcher
        self.resolver = resolver
        self.driver = driver

    @classmethod
    def from_config(
        cls,
        config,
        source_config,
        proxy_manager,
    ) -> Optional['Source']:
        driver_cls_name = source_config.get('driver', {}).get('class', 'nexus.pylon.drivers.BrowserDriver')

        if driver_cls_name.endswith('BrowserDriver') and config.get('webdriver_hub') is None:
            return None

        matcher = Matcher(source_config['matcher'])

        resolver_cls = import_object(
            source_config.get('resolver', {}).get('class', 'nexus.pylon.resolvers.TemplateResolver')
        )
        resolver_args = dict(
            proxy_manager=proxy_manager,
            proxy_list=config['default_resolver_proxy_list'],
        )
        resolver_args.update(**source_config.get('resolver', {}).get('args', {}))
        resolver = resolver_cls(**resolver_args)

        driver_cls = import_object(driver_cls_name)
        driver_args = dict(
            proxy_manager=proxy_manager,
            proxy_list=config['default_driver_proxy_list'],
            config=config,
        )
        driver_args.update(**source_config.get('driver', {}).get('args', {}))
        driver = driver_cls(**driver_args)
        source = Source(matcher=matcher, resolver=resolver, driver=driver)
        return source

    def __str__(self):
        return f'Source({self.resolver}, {self.driver})'

    def is_match(self, params):
        return self.matcher.is_match(params)

    async def download(self, params: Dict) -> AsyncIterable[FileResponsePb]:
        yield FileResponsePb(status=FileResponsePb.Status.RESOLVING)
        async for prepared_file_request in self.resolver.resolve(params):
            try:
                async for resp in self.driver.execute_prepared_file_request(
                    prepared_file_request=prepared_file_request,
                    params=params,
                ):
                    yield resp
                return
            except ClientPayloadError as e:
                logging.getLogger('nexus_pylon').warning(e)
                continue
            except NotFoundError:
                continue
            except DownloadError as e:
                logging.getLogger('nexus_pylon').warning(e)
                continue
        raise NotFoundError(params=params, resolver=str(self.resolver), driver=str(self.driver))
