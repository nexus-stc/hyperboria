import asyncio
import logging
import re
import time
from datetime import (
    datetime,
    timedelta,
)

from aiokit import AioThing
from izihawa_nlptools.regex import DOI_REGEX
from library.telegram.utils import safe_execution
from nexus.views.telegram.scimag import ScimagViewBuilder


class MutualAidService(AioThing):
    def __init__(self, admin_telegram_client, bot_telegram_client, mutual_aid_group_id):
        super().__init__()
        self.admin_telegram_client = admin_telegram_client
        self.bot_telegram_client = bot_telegram_client
        self.mutual_aid_group_id = mutual_aid_group_id
        self.requests = {}
        self.cleanup_task = None

    async def cleanup(self):
        try:
            while 1:
                await self.delete_messages(before_date=time.mktime((datetime.utcnow() - timedelta(hours=46)).timetuple()))
                await self.delete_messages(before_date=time.mktime((datetime.utcnow() - timedelta(hours=2)).timetuple()), document_only=True)
                await asyncio.sleep(3600)
        except asyncio.CancelledError:
            pass

    async def start(self):
        logging.getLogger('debug').debug({
            'action': 'start',
            'mode': 'mutual_aid_service',
            'mutual_aid_group_id': self.mutual_aid_group_id,
        })
        await self.collect_all_requests()
        if not self.cleanup_task:
            self.cleanup_task = asyncio.create_task(self.cleanup())

    async def stop(self):
        if self.cleanup_task:
            self.cleanup_task.cancel()
            await self.cleanup_task
            self.cleanup_task = None

    def is_request(self, message):
        if message.raw_text and message.raw_text.startswith('#request'):
            doi_regex = re.search(DOI_REGEX, message.raw_text)
            if doi_regex:
                return doi_regex.group(1) + '/' + doi_regex.group(2)

    async def collect_all_requests(self):
        async for message in self.admin_telegram_client.iter_messages(self.mutual_aid_group_id):
            if doi := self.is_request(message):
                self.requests[doi] = message.id
        logging.getLogger('debug').debug({
            'action': 'collect',
            'mode': 'mutual_aid_service',
            'requests': len(self.requests)
        })

    async def request(self, doi: str, type_):
        if doi not in self.requests:
            message = await self.bot_telegram_client.send_message(
                self.mutual_aid_group_id,
                f'#request {ScimagViewBuilder.icons.get(type_, ScimagViewBuilder.icon)} https://doi.org/{doi}'
            )
            self.requests[doi] = message.id

    async def delete_request(self, doi: str):
        message_id = self.requests.pop(doi, None)
        logging.getLogger('debug').debug({
            'action': 'delete_request',
            'mode': 'mutual_aid_service',
            'doi': doi,
            'message_id': message_id,
        })
        if message_id:
            async with safe_execution():
                await self.admin_telegram_client.delete_messages(self.mutual_aid_group_id, message_id)

    async def delete_messages(self, before_date, document_only=False):
        messages = []
        async for message in self.admin_telegram_client.iter_messages(self.mutual_aid_group_id):
            if (
                time.mktime(message.date.timetuple()) < before_date
                and (not document_only or message.document)
                and not message.pinned
            ):
                if doi := self.is_request(message):
                    self.requests.pop(doi, None)
                messages.append(message)
        async with safe_execution():
            await self.admin_telegram_client.delete_messages(self.mutual_aid_group_id, messages)
