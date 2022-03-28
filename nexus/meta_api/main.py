import asyncio
import logging

import uvloop
from library.aiogrpctools import AioGrpcServer
from library.configurator import Configurator
from library.logging import configure_logging
from nexus.meta_api.configs import get_config
from nexus.meta_api.providers.data import DataProvider
from nexus.meta_api.providers.stat import StatProvider
from nexus.meta_api.services.documents import DocumentsService
from nexus.meta_api.services.search import SearchService
from summa.aiosumma import SummaClient


class GrpcServer(AioGrpcServer):
    def __init__(self, config):
        self.log_config(config)
        super().__init__(address=config['grpc']['host'], port=config['grpc']['port'])
        self.config = config

        self.summa_client = SummaClient(
            endpoint=config['summa']['endpoint'],
            connection_timeout=config['summa']['connection_timeout'],
        )
        self.data_provider = DataProvider(data_provider_config=self.config['data_provider'])
        self.stat_provider = StatProvider(stat_provider_config=self.config['stat_provider'])

        learn_logger = logging.getLogger('learn') if self.config['application']['learn_log'] else None

        self.search_service = SearchService(
            server=self.server,
            summa_client=self.summa_client,
            stat_provider=self.stat_provider,
            learn_logger=learn_logger,
        )
        self.documents_service = DocumentsService(
            server=self.server,
            summa_client=self.summa_client,
            data_provider=self.data_provider,
            stat_provider=self.stat_provider,
            learn_logger=learn_logger,
        )
        self.waits.extend([self.summa_client, self.data_provider, self.stat_provider,
                          self.search_service, self.documents_service])


async def create_app(config: Configurator):
    try:
        await GrpcServer(config).start_and_wait()
    except asyncio.CancelledError:
        pass


def main():
    config = get_config()
    configure_logging(config)
    if config['metrics']['enabled']:
        from library.metrics_server import MetricsServer
        MetricsServer(config['metrics']).fork_process()
    asyncio.set_event_loop(uvloop.new_event_loop())
    asyncio.get_event_loop().run_until_complete(create_app(config))


if __name__ == '__main__':
    main()
