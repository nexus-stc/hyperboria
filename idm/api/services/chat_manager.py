import sys

from grpc import StatusCode
from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from idm.api.proto.chat_manager_service_pb2 import Chats as ChatsPb
from idm.api.proto.chat_manager_service_pb2_grpc import (
    ChatManagerServicer,
    add_ChatManagerServicer_to_server,
)
from library.aiogrpctools.base import (
    BaseService,
    aiogrpc_request_wrapper,
)
from psycopg.rows import dict_row
from pypika import (
    PostgreSQLQuery,
    Table,
)


class ChatManagerService(ChatManagerServicer, BaseService):
    chats_table = Table('chats')

    async def start(self):
        add_ChatManagerServicer_to_server(self, self.application.server)

    @aiogrpc_request_wrapper()
    async def create_chat(self, request, context, metadata):
        chat = ChatPb(
            chat_id=request.chat_id,
            language=request.language,
            username=request.username,
            is_system_messaging_enabled=True,
            is_discovery_enabled=True,
            is_connectome_enabled=False,
        )
        query = (
            PostgreSQLQuery
            .into(self.chats_table)
            .columns(
                self.chats_table.chat_id,
                self.chats_table.language,
                self.chats_table.username,
                self.chats_table.is_system_messaging_enabled,
                self.chats_table.is_discovery_enabled,
                self.chats_table.is_connectome_enabled,
            )
            .insert(
                chat.chat_id,
                chat.language,
                chat.username,
                chat.is_system_messaging_enabled,
                chat.is_discovery_enabled,
                chat.is_connectome_enabled,
            )
            .on_conflict('chat_id')
            .do_nothing()
        ).get_sql()
        await self.application.pool_holder['idm'].execute(query)
        return await self._get_chat(chat_id=request.chat_id, context=context)

    async def _get_chat(self, chat_id, context):
        sql = (
            PostgreSQLQuery
            .from_(self.chats_table)
            .select(
                self.chats_table.chat_id,
                self.chats_table.username,
                self.chats_table.language,
                self.chats_table.is_system_messaging_enabled,
                self.chats_table.is_discovery_enabled,
                self.chats_table.is_connectome_enabled,
                self.chats_table.ban_until,
                self.chats_table.ban_message,
                self.chats_table.is_admin,
                self.chats_table.created_at,
                self.chats_table.updated_at,
            )
            .where(self.chats_table.chat_id == chat_id)
        ).get_sql()

        chats = [ChatPb(**row) async for row in self.application.pool_holder['idm'].iterate(sql, row_factory=dict_row)]
        if not chats:
            await context.abort(StatusCode.NOT_FOUND, 'not_found')
        return chats[0]

    @aiogrpc_request_wrapper(log=False)
    async def get_chat(self, request, context, metadata):
        return await self._get_chat(chat_id=request.chat_id, context=context)

    @aiogrpc_request_wrapper(log=False)
    async def list_chats(self, request, context, metadata):
        sql = (
            PostgreSQLQuery
            .from_(self.chats_table)
            .select(
                self.chats_table.chat_id,
                self.chats_table.username,
                self.chats_table.language,
                self.chats_table.is_system_messaging_enabled,
                self.chats_table.is_discovery_enabled,
                self.chats_table.is_connectome_enabled,
                self.chats_table.ban_until,
                self.chats_table.ban_message,
                self.chats_table.is_admin,
                self.chats_table.created_at,
                self.chats_table.updated_at,
            )
            .where(self.chats_table.ban_until > request.banned_at_moment)
            .limit(10)
        ).get_sql()
        return ChatsPb(chats=[ChatPb(**row) async for row in self.application.pool_holder['idm'].iterate(sql, row_factory=dict_row)])

    @aiogrpc_request_wrapper()
    async def update_chat(self, request, context, metadata):
        sql = PostgreSQLQuery.update(self.chats_table)
        for field in request.DESCRIPTOR.fields:
            if field.containing_oneof and request.HasField(field.name):
                field_value = getattr(request, field.name)
                sql = sql.set(field.name, field_value)
        sql = sql.where(self.chats_table.chat_id == request.chat_id).returning(
            self.chats_table.chat_id,
            self.chats_table.username,
            self.chats_table.language,
            self.chats_table.is_system_messaging_enabled,
            self.chats_table.is_discovery_enabled,
            self.chats_table.is_connectome_enabled,
            self.chats_table.ban_until,
            self.chats_table.ban_message,
            self.chats_table.is_admin,
            self.chats_table.created_at,
            self.chats_table.updated_at,
        ).get_sql()
        rows = []
        async for row in self.application.pool_holder['idm'].iterate(sql, row_factory=dict_row):
            rows.append(row)
        if not rows:
            return await context.abort(StatusCode.NOT_FOUND, 'not_found')
        return ChatPb(**rows[0])
