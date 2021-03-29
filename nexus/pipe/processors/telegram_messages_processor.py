import time
from typing import Iterable

from library.nlptools.language_detect import detect_language
from library.nlptools.utils import (
    clean_text,
    replace_telegram_link,
)
from pypika import (
    PostgreSQLQuery,
    Table,
)

from .base import BaseDatabaseProcessor


class TelegramMessagesProcessor(BaseDatabaseProcessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telegram_messages_table = Table('telegram_messages')

    def generate_delete_sql(self, telegram_message_pb):
        return (
            PostgreSQLQuery
            .from_('telegram_messages')
            .where(self.telegram_messages_table.id == telegram_message_pb.id)
            .delete()
            .get_sql()
        )

    def generate_insert_sql(self, telegram_message_pb):
        return (
            PostgreSQLQuery
            .into('telegram_messages')
            .columns(
                'channel_id',
                'message_id',
                'is_deleted',
                'text',
                'clean_text',
                'lang',
                'message_type',
                'unixtime',
                'views'
            )
            .insert(
                telegram_message_pb.channel_id,
                telegram_message_pb.message_id,
                telegram_message_pb.is_deleted,
                telegram_message_pb.text,
                telegram_message_pb.clean_text,
                telegram_message_pb.language,
                telegram_message_pb.message_type,
                telegram_message_pb.unixtime,
                telegram_message_pb.views,
            )
            .on_conflict(self.telegram_messages_table.channel_id, self.telegram_messages_table.message_id)
            .do_update(self.telegram_messages_table.is_deleted, telegram_message_pb.is_deleted)
            .do_update(self.telegram_messages_table.text, telegram_message_pb.text)
            .do_update(self.telegram_messages_table.clean_text, telegram_message_pb.clean_text)
            .do_update(self.telegram_messages_table.lang, telegram_message_pb.language)
            .do_update(self.telegram_messages_table.message_type, telegram_message_pb.message_type)
            .do_update(self.telegram_messages_table.views, telegram_message_pb.views)
            .returning(self.telegram_messages_table.id)
            .get_sql()
        )

    async def process_bulk(self, messages: Iterable):
        return
        insert_sqls = []
        delete_sqls = []
        documents_container_pb = DocumentsContainerPb()
        update_document_operations_pb = []

        current_time = int(time.time())

        for document_operation_pb in messages:
            if document_operation_pb.WhichOneof('operation') == 'update_document':
                document_pb = document_operation_pb.update_document.document
                telegram_message_pb = document_pb.telegram_message

                if telegram_message_pb.is_deleted and telegram_message_pb.id:
                    delete_sqls.append(self.generate_delete_sql(telegram_message_pb))
                    documents_container_pb.documents.append(document_pb)
                else:
                    telegram_message_pb.clean_text = clean_text(replace_telegram_link(telegram_message_pb.text))
                    telegram_message_pb.language = detect_language(telegram_message_pb.clean_text) or ''

                    insert_sqls.append(self.generate_insert_sql(telegram_message_pb))
                    update_document_operations_pb.append(document_operation_pb)

        if insert_sqls:
            for insert_sql, update_document_operation_pb in zip(insert_sqls, update_document_operations_pb):
                result = await self.pool_holder.execute(insert_sql, fetch=True)

                document_pb = update_document_operation_pb.update_document.document
                telegram_message_pb = document_pb.telegram_message

                telegram_message_pb.id = result[0][0]
                if update_document_operation_pb.update_document.reindex:
                    if (
                        len(telegram_message_pb.clean_text) > 120
                        and telegram_message_pb.unixtime > current_time - 60 * 24 * 60 * 60
                        and telegram_message_pb.message_type == TelegramMessagePb.Type.TEXTUAL
                    ):
                        documents_container_pb.documents.append(document_pb)
        if delete_sqls:
            await self.pool_holder.execute(';'.join(delete_sqls))
