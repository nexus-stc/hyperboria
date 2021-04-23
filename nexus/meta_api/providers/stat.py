import asyncio
import logging
from contextlib import asynccontextmanager

from aiochclient import ChClient
from aiohttp import ClientSession
from aiokit import AioThing
from recordclass import dataobject


class DocumentStat(dataobject):
    downloads_count: int


class StatProvider(AioThing):
    def __init__(self, stat_provider_config):
        super().__init__()
        self.stat_provider_config = stat_provider_config
        self.clickhouse_session = None
        self.clickhouse_client = None
        self.download_stats = {}
        self.top_missed_stats = []
        self.current_task = None

        if stat_provider_config['enabled']:
            self.clickhouse_session = ClientSession()
            self.clickhouse_client = ChClient(
                self.clickhouse_session,
                url=stat_provider_config['clickhouse']['host'],
                user=stat_provider_config['clickhouse']['username'],
                password=stat_provider_config['clickhouse']['password'],
            )

    @asynccontextmanager
    async def _safe_execution(self):
        try:
            yield
        except asyncio.CancelledError as e:
            logging.getLogger('error').warning(e)
        except Exception as e:
            logging.getLogger('error').error(e)
            raise

    async def load_download_stats(self):
        async with self._safe_execution():
            download_stats = {}
            logging.getLogger('statbox').info({
                'action': 'start_loading',
                'stats': 'download_stats',
            })
            async for row in self.clickhouse_client.iterate('''
                select id, count(distinct user_id) as c
                from query_log where mode = 'get' and id != 0
                group by id
            '''):
                download_stats[row['id']] = DocumentStat(downloads_count=row['c'])
            self.download_stats = download_stats
            logging.getLogger('statbox').info({
                'action': 'loaded',
                'stats': 'download_stats',
                'items': len(download_stats),
            })
            await asyncio.sleep(self.stat_provider_config['download_stats']['refresh_time_secs'])

    async def load_top_missed_stats(self):
        async with self._safe_execution():
            top_missed_stats = []
            logging.getLogger('statbox').info({
                'action': 'start_loading',
                'stats': 'top_missing',
            })
            async for row in self.clickhouse_client.iterate('''
                select
                document_id,
                count(distinct chat_id) as c from telegram_statbox_log
                where action = 'missed' and
                (mode = 'start_delivery' or mode = 'delivery') and
                schema = 'scimag'
                group by document_id
                order by count(distinct chat_id) desc, document_id desc limit 1000
            '''):
                top_missed_stats.append(row['document_id'])
            self.top_missed_stats = top_missed_stats
            logging.getLogger('statbox').info({
                'action': 'loaded',
                'stats': 'top_missing',
                'items': len(top_missed_stats),
            })
            await asyncio.sleep(self.stat_provider_config['top_missed_stats']['refresh_time_secs'])

    def get_download_stats(self, document_id, default=None):
        return self.download_stats.get(document_id, default)

    def get_top_missed_stats(self):
        return self.top_missed_stats

    async def all_tasks(self):
        return await asyncio.gather(
            self.load_download_stats(),
            self.load_top_missed_stats(),
        )

    async def start(self):
        if self.clickhouse_session:
            self.current_task = asyncio.create_task(self.all_tasks())

    async def stop(self):
        await self.cancel()
        if self.clickhouse_session:
            await self.clickhouse_session.close()
        if self.current_task:
            self.current_task.cancel()
            await self.current_task
        await super().stop()
