import asyncio

import uvloop
from library.aiogrpctools import AioGrpcServer
from library.aiopostgres import AioPostgresPoolHolder
from library.configurator import Configurator
from library.logging import configure_logging
from library.telegram.base import BaseTelegramClient
from nexus.hub.configs import get_config
from nexus.hub.services.delivery import DeliveryService
from nexus.hub.services.submitter import SubmitterService


class GrpcServer(AioGrpcServer):
    def __init__(self, config: Configurator):
        self.log_config(config)
        super().__init__(address=config['grpc']['address'], port=config['grpc']['port'])

        self.pool_holder = None
        if config['database']['enabled']:
            self.pool_holder = AioPostgresPoolHolder(
                conninfo=f'dbname={config["database"]["database"]} '
                f'user={config["database"]["username"]} '
                f'password={config["database"]["password"]} '
                f'host={config["database"]["host"]}',
            )
            self.waits.append(self.pool_holder)

        self.telegram_clients = {}
        for telegram_bot in config['telegram']['bots']:
            telegram_bot_config = config['telegram']['bots'][telegram_bot]
            telegram_client = BaseTelegramClient(
                app_id=telegram_bot_config['app_id'],
                app_hash=telegram_bot_config['app_hash'],
                bot_token=telegram_bot_config['bot_token'],
                database=telegram_bot_config.get('database'),
                mtproxy=telegram_bot_config.get('mtproxy'),
            )
            self.telegram_clients[telegram_bot] = telegram_client
        self.starts.extend(self.telegram_clients.values())

        self.delivery_service = DeliveryService(
            server=self.server,
            service_name=config['application']['service_name'],
            ipfs_config=config['ipfs'],
            is_sharience_enabled=config['application']['is_sharience_enabled'],
            maintenance_picture_url=config['application'].get('maintenance_picture_url', ''),
            pool_holder=self.pool_holder,
            pylon_config=config['pylon'],
            should_store_hashes=config['application']['should_store_hashes'],
            telegram_clients=self.telegram_clients,
            telegram_bot_configs=config['telegram']['bots'],
        )
        self.starts.append(self.delivery_service)

        if config['grobid']['enabled']:
            self.submitter_service = SubmitterService(
                server=self.server,
                service_name=config['application']['service_name'],
                grobid_config=config['grobid'],
                ipfs_config=config['ipfs'],
                meta_api_config=config['meta_api'],
                telegram_clients=self.telegram_clients,
            )
            self.starts.append(self.submitter_service)


def main():
    config = get_config()
    configure_logging(config)
    uvloop.install()
    grpc_server = GrpcServer(config)
    asyncio.get_event_loop().run_until_complete(grpc_server.start_and_wait())


if __name__ == '__main__':
    main()
