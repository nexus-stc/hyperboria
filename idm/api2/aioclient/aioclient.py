from aiokit import AioThing
from grpc import StatusCode
from grpc.experimental.aio import (
    AioRpcError,
    insecure_channel,
)
from idm.api2.proto.chats_service_pb2 import (
    CreateChatRequest,
    GetChatRequest,
    ListChatsRequest,
    UpdateChatRequest,
)
from idm.api2.proto.chats_service_pb2_grpc import ChatsStub
from lru import LRU
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_fixed,
)


class IdmApi2GrpcClient(AioThing):
    def __init__(
        self,
        base_url,
    ):
        super().__init__()
        self.channel = insecure_channel(base_url, [
            ('grpc.dns_min_time_between_resolutions_ms', 1000),
            ('grpc.initial_reconnect_backoff_ms', 1000),
            ('grpc.lb_policy_name', 'round_robin'),
            ('grpc.min_reconnect_backoff_ms', 1000),
            ('grpc.max_reconnect_backoff_ms', 2000),
        ])
        self.chats_stub = ChatsStub(self.channel)
        self.cache = LRU(4096)

    async def start(self):
        await self.channel.channel_ready()

    async def stop(self):
        await self.channel.close()

    async def create_chat(
        self,
        chat_id,
        username,
        language,
        request_id: str = None,
    ):
        response = await self.chats_stub.create_chat(
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

    @retry(
        retry=retry_if_exception(
            lambda e: isinstance(e, AioRpcError) and e.code() == StatusCode.UNAVAILABLE
        ),
        reraise=True,
        stop=stop_after_attempt(10),
        wait=wait_fixed(5),
    )
    async def get_chat(
        self,
        chat_id,
        request_id: str = None,
    ):
        response = await self.chats_stub.get_chat(
            GetChatRequest(chat_id=chat_id),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response

    async def list_chats(
        self,
        request_id: str = None,
        banned_at_moment=None,
    ):
        response = await self.chats_stub.list_chats(
            ListChatsRequest(banned_at_moment=banned_at_moment),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response

    async def update_chat(
        self,
        chat_id,
        request_id: str = None,
        language=None,
        is_system_messaging_enabled=None,
        is_discovery_enabled=None,
        ban_until=None,
        ban_message=None,
        is_admin=None,
        last_location=None,
    ):
        response = await self.chats_stub.update_chat(
            UpdateChatRequest(
                chat_id=chat_id,
                language=language,
                is_system_messaging_enabled=is_system_messaging_enabled,
                is_discovery_enabled=is_discovery_enabled,
                ban_until=ban_until,
                ban_message=ban_message,
                is_admin=is_admin,
                last_location=last_location,
            ),
            metadata=(
                ('request-id', request_id),
            ),
        )
        return response
