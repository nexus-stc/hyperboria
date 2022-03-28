import logging

from grpc import StatusCode
from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from idm.api.proto.chat_manager_service_pb2 import Chats as ChatsPb
from idm.api.proto.chat_manager_service_pb2_grpc import (
    ChatManagerServicer,
    add_ChatManagerServicer_to_server,
)
from izihawa_utils.pb_to_json import MessageToDict
from library.aiogrpctools.base import (
    BaseService,
    aiogrpc_request_wrapper,
)
from pypika import (
    PostgreSQLQuery,
    Table,
)


class ChatManagerService(ChatManagerServicer, BaseService):
    chats_table = Table('chats')

    def __init__(self, server, service_name, pool_holder):
        super().__init__(service_name=service_name)
        self.server = server
        self.pool_holder = pool_holder

    async def start(self):
        add_ChatManagerServicer_to_server(self, self.server)

    @aiogrpc_request_wrapper()
    async def create_chat(self, request, context, metadata):
        chat = ChatPb(
            chat_id=request.chat_id,
            language=request.language,
            username=request.username,
            is_system_messaging_enabled=True,
            is_discovery_enabled=True,
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
            )
            .insert(
                chat.chat_id,
                chat.language,
                chat.username,
                chat.is_system_messaging_enabled,
                chat.is_discovery_enabled,
            )
            .on_conflict('chat_id')
            .do_nothing()
        ).get_sql()
        async with self.pool_holder.pool.acquire() as session:
            await session.execute(query)
            return await self._get_chat(session=session, chat_id=request.chat_id, context=context)

    async def _get_chat(self, session, chat_id, context):
        query = (
            PostgreSQLQuery
            .from_(self.chats_table)
            .select('*')
            .where(self.chats_table.chat_id == chat_id)
        ).get_sql()
        result = await session.execute(query)
        chat = await result.fetchone()
        if chat is None:
            await context.abort(StatusCode.NOT_FOUND, 'not_found')
        return ChatPb(**chat)

    @aiogrpc_request_wrapper()
    async def get_chat(self, request, context, metadata):
        async with self.pool_holder.pool.acquire() as session:
            return await self._get_chat(session=session, chat_id=request.chat_id, context=context)

    @aiogrpc_request_wrapper()
    async def list_chats(self, request, context, metadata):
        query = (
            PostgreSQLQuery
            .from_(self.chats_table)
            .select('*')
            .where(self.chats_table.ban_until > request.banned_at_moment)
            .limit(10)
        ).get_sql()
        async with self.pool_holder.pool.acquire() as session:
            results = await session.execute(query)
            chats = await results.fetchall()
            return ChatsPb(
                chats=list(map(lambda x: ChatPb(**x), chats))
            )

    @aiogrpc_request_wrapper()
    async def update_chat(self, request, context, metadata):
        query = PostgreSQLQuery.update(self.chats_table)
        for field in request.DESCRIPTOR.fields:
            if field.containing_oneof and request.HasField(field.name):
                field_value = getattr(request, field.name)
                query = query.set(field.name, field_value)
        query = query.where(self.chats_table.chat_id == request.chat_id).returning('*').get_sql()
        async with self.pool_holder.pool.acquire() as session:
            result = await session.execute(query)
            chat = await result.fetchone()
        return ChatPb(**chat)
