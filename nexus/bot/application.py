from aiokit import AioRootThing
from idm.api.aioclient import IdmApiGrpcClient
from izihawa_utils.importlib import import_object
from library.telegram.base import BaseTelegramClient
from library.telegram.promotioner import Promotioner
from nexus.bot.user_manager import UserManager
from nexus.hub.aioclient import HubGrpcClient
from nexus.meta_api.aioclient import MetaApiGrpcClient
from nexus.promotions import get_promotions


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
            catch_up=self.config['telegram'].get('catch_up', False)
        )
        self.hub_client = HubGrpcClient(endpoint=self.config['hub']['endpoint'])
        self.starts.append(self.hub_client)
        self.idm_client = None
        if self.config['idm']['enabled']:
            self.idm_client = IdmApiGrpcClient(endpoint=self.config['idm']['endpoint'])
            self.starts.append(self.idm_client)
        self.meta_api_client = MetaApiGrpcClient(endpoint=self.config['meta_api']['endpoint'])
        self.starts.append(self.meta_api_client)

        self.promotioner = Promotioner(
            promotions=get_promotions(),
            promotion_vars=dict(
                mutual_aid_group=self.config['telegram']['mutual_aid_group'],
                twitter_contact_url=self.config['twitter']['contact_url'],
                related_channel=self.config['telegram']['related_channel'],
            )
        )
        self.user_manager = UserManager()
        self._handlers = []

    def set_handlers(self, telegram_client):
        for handler in self.config['telegram']['handlers']:
            import_object(handler)(self).register_for(telegram_client)

    async def start(self):
        self.set_handlers(self.telegram_client)
        await self.telegram_client.start()

    async def stop(self):
        self.telegram_client.remove_event_handlers()
        await self.telegram_client.stop()
