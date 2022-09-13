import asyncio

import uvloop
from aiochclient import ChClient
from aiohttp import ClientSession
from idm.api.configs import get_config
from idm.api.services.chat_manager import ChatManagerService
from idm.api.services.profile import ProfileService
from idm.api.services.subscription_manager import SubscriptionManagerService
from izihawa_configurator import Configurator
from library.aiogrpctools import AioGrpcServer
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from library.logging import configure_logging


class GrpcServer(AioGrpcServer):
    def __init__(self, config: Configurator):
        super().__init__(address=config['grpc']['address'], port=config['grpc']['port'])
        database = config['database']
        self.pool_holder = {
            'idm': AioPostgresPoolHolder(
                conninfo=f'dbname={database["idm"]["database"]} user={database["idm"]["username"]} '
                         f'password={database["idm"]["password"]} host={database["idm"]["host"]} port={database["idm"]["port"]}',
                timeout=30,
                max_size=4,
            ),
            'nexus': AioPostgresPoolHolder(
                conninfo=f'dbname={database["nexus"]["database"]} user={database["nexus"]["username"]} '
                         f'password={database["nexus"]["password"]} host={database["nexus"]["host"]} port={database["nexus"]["port"]}',
                timeout=30,
                max_size=4,
            )
        }
        self.starts.extend([self.pool_holder['idm'], self.pool_holder['nexus']])
        self.chat_manager_service = ChatManagerService(
            application=self,
            service_name=config['application']['service_name'],
        )
        self.subscription_manager_service = SubscriptionManagerService(
            application=self,
            service_name=config['application']['service_name'],
        )
        self.clickhouse_session = ClientSession()
        self.clickhouse_client = ChClient(
            self.clickhouse_session,
            url=config['clickhouse']['host'],
            user=config['clickhouse']['username'],
            password=config['clickhouse']['password'],
        )
        self.profile_service = ProfileService(
            application=self,
            service_name=config['application']['service_name'],
        )
        self.starts.extend([self.chat_manager_service, self.profile_service, self.subscription_manager_service])


def main():
    config = get_config()
    configure_logging(config)
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    grpc_server = GrpcServer(config)
    loop.run_until_complete(grpc_server.start_and_wait())


if __name__ == '__main__':
    main()
