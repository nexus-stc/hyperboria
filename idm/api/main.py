import asyncio

import uvloop
from aiopg.sa import create_engine
from idm.api.configs import get_config
from idm.api.daemons.admin_log_reader import AdminLogReader
from idm.api.services.chat_manager import ChatManagerService
from library.aiogrpctools import AioGrpcServer
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from library.configurator import Configurator
from library.logging import configure_logging


class GrpcServer(AioGrpcServer):
    def __init__(self, config: Configurator):
        super().__init__(address=config['grpc']['address'], port=config['grpc']['port'])
        self.pool_holder = AioPostgresPoolHolder(
            fn=create_engine,
            database=config['database']['database'],
            user=config['database']['username'],
            password=config['database']['password'],
            host=config['database']['host'],
            port=config['database']['port'],
            timeout=30,
            pool_recycle=60,
            maxsize=4,
        )
        self.admin_log_reader = AdminLogReader(
            telegram_config=config['telegram'],
        )
        self.chat_manager_service = ChatManagerService(
            server=self.server,
            service_name=config['application']['service_name'],
            pool_holder=self.pool_holder,
            admin_log_reader=self.admin_log_reader,
        )
        self.starts.append(self.admin_log_reader)
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
