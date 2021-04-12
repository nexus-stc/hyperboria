import asyncio
import logging
import string

from aiokit import AioThing
from library.telegram.base import BaseTelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


class AdminLogReader(AioThing):
    channel_name = '@nexus_search'

    def __init__(self, telegram_config):
        super().__init__()
        self.subscriptors = set()
        self.loading = False
        self.telegram_client = BaseTelegramClient(
            app_id=telegram_config['app_id'],
            app_hash=telegram_config['app_hash'],
            database=telegram_config['database'],
            flood_sleep_threshold=25,
        )
        self.last_max_id = 0

    def statbox(self, **kwargs):
        logging.getLogger('statbox').info({'mode': 'admin_log_reader', **kwargs})

    async def skip_admin_log(self):
        async for event in self.telegram_client.iter_admin_log(self.channel_name, limit=1):
            self.last_max_id = event.id
        self.statbox(action='skipped_admin_log', max_id=self.last_max_id)

    async def process_admin_log(self, sleep=1.0):
        self.loading = True
        try:
            while 1:
                async for event in self.telegram_client.iter_admin_log(
                    self.channel_name, join=True, invite=True, leave=True, min_id=self.last_max_id
                ):
                    is_subscribed = event.joined or event.joined_invite
                    if is_subscribed:
                        self.subscriptors.add(event.user_id)
                    elif event.user_id in self.subscriptors:
                        self.subscriptors.remove(event.user_id)
                    self.last_max_id = event.id
                await asyncio.sleep(sleep)
        except asyncio.CancelledError:
            pass
        finally:
            self.loading = False

    async def _fetch_users(self, query):
        max_batch_size = 200

        participants = await self.telegram_client(
            GetParticipantsRequest(
                channel=self.channel_name,
                filter=ChannelParticipantsSearch(query),
                offset=0,
                limit=max_batch_size,
                hash=0,
            )
        )

        for user in participants.users:
            self.subscriptors.add(user.id)

        # There is a possibility that more users exist if we hit maximum count of users
        # So, we are making a recursion to reveal it
        if len(participants.users) == max_batch_size:
            for new_letter in string.ascii_lowercase + string.digits:
                await self._fetch_users(query + new_letter)

    async def load_channel_users(self):
        self.statbox(action='load_channel_users')
        await self._fetch_users('')
        self.statbox(action='loaded_channel_users', subscriptors=len(self.subscriptors))

    async def start(self):
        await self.telegram_client.start_and_wait()
        await self.skip_admin_log()
        await self.load_channel_users()
        asyncio.create_task(self.process_admin_log())

    def is_subscribed(self, user_id):
        return not self.loading or user_id in self.subscriptors
