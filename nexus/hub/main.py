import asyncio
import logging

import uvloop
from aiogrobid import GrobidClient
from aioipfs import AsyncIPFS as AsyncIPFS
from idm.api.aioclient import IdmApiGrpcClient
from library.aiogrpctools import AioGrpcServer
from library.aiopostgres import AioPostgresPoolHolder
from library.configurator import Configurator
from library.logging import configure_logging
from library.telegram.base import BaseTelegramClient
from nexus.hub.configs import get_config
from nexus.hub.services.delivery import DeliveryService
from nexus.hub.services.mutual_aid_service import MutualAidService
from nexus.hub.services.submitter import SubmitterService
from nexus.hub.user_manager import UserManager
from nexus.meta_api.aioclient import MetaApiGrpcClient


class GrpcServer(AioGrpcServer):
    def __init__(self, config: Configurator):
        self.log_config(config)
        self.config = config
        super().__init__(address=config['grpc']['address'], port=config['grpc']['port'])

        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={config["database"]["database"]} '
                     f'user={config["database"]["username"]} '
                     f'password={config["database"]["password"]} '
                     f'host={config["database"]["host"]}',
        )
        self.starts.append(self.pool_holder)

        self.telegram_clients = {}
        self.mutual_aid_services = {}

        telegram_bot_config = config['telegram']['admin']
        self.admin_telegram_client = BaseTelegramClient(
            app_id=telegram_bot_config['app_id'],
            app_hash=telegram_bot_config['app_hash'],
            database=telegram_bot_config.get('database'),
            mtproxy=telegram_bot_config.get('mtproxy'),
            phone=telegram_bot_config['phone'],
        )

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
            if mutual_aid_group_id := telegram_bot_config.get('mutual_aid_group_id'):
                self.mutual_aid_services[telegram_bot] = MutualAidService(
                    admin_telegram_client=self.admin_telegram_client,
                    bot_telegram_client=telegram_client,
                    mutual_aid_group_id=mutual_aid_group_id,
                )
        self.starts.append(self.admin_telegram_client)
        self.starts.extend(self.telegram_clients.values())
        self.starts.extend(self.mutual_aid_services.values())

        self.grobid_client = GrobidClient(base_url=config['grobid']['url'])
        self.idm_client = IdmApiGrpcClient(endpoint=config['idm']['endpoint'])
        self.ipfs_client = AsyncIPFS(host=config['ipfs']['address'], port=config['ipfs']['port'])
        self.meta_api_client = MetaApiGrpcClient(endpoint=config['meta_api']['endpoint'])
        self.starts.extend([self.grobid_client, self.idm_client, self.ipfs_client, self.meta_api_client])
        self.user_manager = UserManager()

        self.delivery_service = DeliveryService(
            application=self,
            service_name=config['application']['service_name'],
            is_sharience_enabled=config['application']['is_sharience_enabled'],
            maintenance_picture_url=config['application'].get('maintenance_picture_url', ''),
            should_parse_with_grobid=config['application']['should_parse_with_grobid'],
            should_store_hashes=config['application']['should_store_hashes'],
            telegram_bot_configs=config['telegram']['bots'],
            pylon_config=config['pylon'],
        )
        self.submitter_service = SubmitterService(
            application=self,
            service_name=config['application']['service_name'],
        )
        self.starts.extend([self.delivery_service, self.submitter_service])


def main():
    config = get_config()
    configure_logging(config)
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    grpc_server = GrpcServer(config)
    return loop.run_until_complete(grpc_server.start_and_wait())


if __name__ == '__main__':
    result = main()
    logging.getLogger('debug').debug({
        'action': 'exit',
        'mode': 'main',
        'result': str(result)
    })
