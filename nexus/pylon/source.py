import logging
from typing import (
    AsyncIterable,
    Dict,
    List,
)

from aiohttp.client_exceptions import ClientPayloadError
from library.aiokit.aiokit import AioThing
from library.logging import error_log
from nexus.pylon.drivers.base import BaseDriver
from nexus.pylon.exceptions import (
    DownloadError,
    NotFoundError,
)
from nexus.pylon.matcher import Matcher
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.pylon.resolvers.base import BaseResolver
from utils.izihawa_utils.importlib import import_object


class Source(AioThing):
    def __init__(self, matcher: Matcher, resolver: BaseResolver, driver: BaseDriver):
        super().__init__()
        self.matcher = matcher
        self.resolver = resolver
        self.driver = driver

    @classmethod
    def from_config(
        cls,
        proxy_manager,
        source_config,
        downloads_directory: str,
        default_driver_proxy_list: List,
        default_resolver_proxy_list: List,
    ) -> 'Source':
        matcher = Matcher(source_config['matcher'])

        resolver_cls = import_object(
            source_config.get('resolver', {}).get('class', 'nexus.pylon.resolvers.TemplateResolver')
        )
        resolver_args = dict(
            proxy_manager=proxy_manager,
            proxy_list=default_resolver_proxy_list,
        )
        resolver_args.update(**source_config.get('resolver', {}).get('args', {}))
        resolver = resolver_cls(**resolver_args)

        driver_cls = import_object(source_config.get('driver', {}).get('class', 'nexus.pylon.drivers.BrowserDriver'))
        driver_args = dict(
            proxy_manager=proxy_manager,
            downloads_directory=downloads_directory,
            proxy_list=default_driver_proxy_list,
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
            logging.debug({
                'action': 'download',
                'mode': 'pylon',
                'params': params,
                'source': str(self),
                'url': prepared_file_request.url,
            })
            try:
                async for resp in self.driver.execute_prepared_file_request(
                    prepared_file_request=prepared_file_request,
                    params=params,
                ):
                    yield resp
                return
            except ClientPayloadError as e:
                error_log(e, level=logging.WARNING)
                continue
            except NotFoundError:
                continue
            except DownloadError as e:
                error_log(e)
                continue
        raise NotFoundError(params=params, resolver=str(self.resolver), driver=str(self.driver))
