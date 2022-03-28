import asyncio

import uvloop
from idm.api.configs import get_config
from idm.api.services.chat_manager import ChatManagerService
from library.aiogrpctools import AioGrpcServer
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from library.configurator import Configurator
from library.logging import configure_logging


class GrpcServer(AioGrpcServer):
    def __init__(self, config: Configurator):
        super().__init__(address=config['grpc']['address'], port=config['grpc']['port'])
        database = config['database']
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
                f'user={database["username"]} '
                f'password={database["password"]} '
                f'host={database["host"]}'
                f'port={database["port"]}',
            timeout=30,
            max_size=4,
        )
        self.chat_manager_service = ChatManagerService(
            server=self.server,
            service_name=config['application']['service_name'],
            pool_holder=self.pool_holder,
        )
        self.waits.extend([self.chat_manager_service, self.pool_holder])


async def create_app(config: Configurator):
    grpc_server = GrpcServer(config)
    await grpc_server.start_and_wait()


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
