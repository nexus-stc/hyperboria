from typing import Optional

from aiogrpcclient import BaseGrpcClient
from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from idm.api.proto.chat_manager_service_pb2 import Chats as ChatsPb
from idm.api.proto.chat_manager_service_pb2 import (
    CreateChatRequest,
    GetChatRequest,
    ListChatsRequest,
    UpdateChatRequest,
)
from idm.api.proto.chat_manager_service_pb2_grpc import ChatManagerStub


class IdmApiGrpcClient(BaseGrpcClient):
    stub_clses = {
        'chat_manager': ChatManagerStub,
    }

    async def create_chat(
        self,
        chat_id: int,
        username: str,
        language: str,
        request_id: Optional[str] = None,
    ) -> ChatPb:
        response = await self.stubs['chat_manager'].create_chat(
            CreateChatRequest(
                chat_id=chat_id,
                username=username,
                language=language,
            ),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response

    async def get_chat(
        self,
        chat_id: int,
        request_id: Optional[str] = None,
    ) -> ChatPb:
        response = await self.stubs['chat_manager'].get_chat(
            GetChatRequest(chat_id=chat_id),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response

    async def list_chats(
        self,
        request_id: Optional[str] = None,
        banned_at_moment: Optional[str] = None,
    ) -> ChatsPb:
        response = await self.stubs['chat_manager'].list_chats(
            ListChatsRequest(banned_at_moment=banned_at_moment),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response

    async def update_chat(
        self,
        chat_id: int,
        request_id: Optional[str] = None,
        language: Optional[str] = None,
        is_system_messaging_enabled: Optional[bool] = None,
        is_discovery_enabled: Optional[bool] = None,
        ban_until: Optional[int] = None,
        ban_message: Optional[str] = None,
        is_admin: Optional[bool] = None,
    ) -> ChatPb:
        response = await self.stubs['chat_manager'].update_chat(
            UpdateChatRequest(
                chat_id=chat_id,
                language=language,
                is_system_messaging_enabled=is_system_messaging_enabled,
                is_discovery_enabled=is_discovery_enabled,
                ban_until=ban_until,
                ban_message=ban_message,
                is_admin=is_admin,
            ),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response
