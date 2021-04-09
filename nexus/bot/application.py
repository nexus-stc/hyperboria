from aiokit import AioRootThing
from idm.api2.aioclient import IdmApi2GrpcClient
from izihawa_utils.importlib import import_object
from library.telegram.base import BaseTelegramClient
from nexus.bot.promotioner import Promotioner
from nexus.bot.user_manager import UserManager
from nexus.hub.aioclient import HubGrpcClient
from nexus.meta_api.aioclient import MetaApiGrpcClient


class TelegramApplication(AioRootThing):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.telegram_client = BaseTelegramClient(
            app_id=self.config['telegram']['app_id'],
            app_hash=self.config['telegram']['app_hash'],
            bot_token=self.config['telegram']['bot_token'],
            database=self.config['telegram'].get('database'),
            mtproxy=self.config['telegram'].get('mtproxy'),
        )

        self.hub_client = HubGrpcClient(base_url=self.config['hub']['url'])
        self.idm_client = IdmApi2GrpcClient(base_url=self.config['idm']['url'])
        self.meta_api_client = MetaApiGrpcClient(base_url=self.config['meta_api']['url'])

        self.promotioner = Promotioner(promotions=self.config['promotions'])
        self.user_manager = UserManager()
        self._handlers = []

        self.starts.extend([self.hub_client, self.idm_client, self.meta_api_client])

    def set_handlers(self, telegram_client):
        for handler in self.config['telegram']['handlers']:
            import_object(handler)(self).register_for(telegram_client)

    async def start(self):
        self.set_handlers(self.telegram_client)
        await self.telegram_client.start_and_wait()
        await self.telegram_client.run_until_disconnected()

    async def stop(self):
        self.telegram_client.remove_event_handlers()
        await self.telegram_client.stop()
