from typing import List

import aiopg
from aiokit import AioThing
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from recordclass import dataobject


class DocumentData(dataobject):
    ipfs_multihashes: List[str]
    telegram_file_id: int


class DataProvider(AioThing):
    def __init__(self, data_provider_config: dict):
        super().__init__()
        self.pool_holder = None
        if data_provider_config['enabled']:
            self.pool_holder = AioPostgresPoolHolder(
                fn=aiopg.create_pool,
                dsn=f'dbname={data_provider_config["database"]} '
                f'user={data_provider_config["username"]} '
                f'password={data_provider_config["password"]} '
                f'host={data_provider_config["host"]}',
                timeout=30,
                pool_recycle=60,
                maxsize=4,
            )
            self.waits.append(self.pool_holder)

    async def get(self, document_id):
        if not self.pool_holder:
            return
        pg_data = await self.pool_holder.execute('''
            select id, telegram_file_id, ipfs_multihashes
            from scimag
            where id = %s
            union all
            select id, telegram_file_id, ipfs_multihashes
            from scitech
            where id = %s
        ''', (document_id, document_id), fetch=True)
        for _, telegram_file_id, ipfs_multihashes in pg_data:
            return DocumentData(
                ipfs_multihashes=ipfs_multihashes or [],
                telegram_file_id=telegram_file_id or '',
            )

    async def random_id(self, language):
        if not self.pool_holder:
            return
        pg_data = await self.pool_holder.execute('''
            select id from scitech
            where
                (language = %s or language = 'en')
                and original_id is null
                and is_deleted = false
            offset floor(
                random() * (
                    select count(*) from scitech where
                        (language = %s or language = 'en')
                        and original_id is null
                        and is_deleted = false
                    )
                )
            limit 1;
        ''', (language, language), fetch=True)
        for (id_,) in pg_data:
            return id_
