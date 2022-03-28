from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from pypika import (
    PostgreSQLQuery,
    Table,
)

from ..base import BaseAction


class ToPostgresAction(BaseAction):
    telegram_files_table = Table('telegram_files')

    def __init__(self, database):
        super().__init__()
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
        )
        self.waits.append(self.pool_holder)

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        store_telegram_file_id_pb = document_operation_pb.store_telegram_file_id

        query = (
            PostgreSQLQuery
            .into(self.telegram_files_table)
            .columns('bot_name', 'document_id', 'telegram_file_id')
            .insert(
                store_telegram_file_id_pb.bot_name,
                store_telegram_file_id_pb.document_id,
                store_telegram_file_id_pb.telegram_file_id,
            )
            .on_conflict('bot_name', 'document_id')
            .do_nothing()
        )
        await self.pool_holder.execute(query.get_sql())
        return document_operation_pb
