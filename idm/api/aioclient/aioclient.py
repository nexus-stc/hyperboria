from typing import (
    Optional,
    TypedDict,
    Union,
)

from aiogrpcclient import BaseGrpcClient
from idm.api.proto import (
    chat_manager_service_pb2,
    chat_manager_service_pb2_grpc,
    profile_service_pb2,
    profile_service_pb2_grpc,
    subscription_manager_service_pb2,
    subscription_manager_service_pb2_grpc,
)


class IdmApiGrpcClient(BaseGrpcClient):
    stub_clses = {
        'chat_manager': chat_manager_service_pb2_grpc.ChatManagerStub,
        'profile': profile_service_pb2_grpc.ProfileStub,
        'subscription_manager': subscription_manager_service_pb2_grpc.SubscriptionManagerStub,
    }

    async def create_chat(
        self,
        chat_id: int,
        username: str,
        language: str,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> chat_manager_service_pb2.Chat:
        response = await self.stubs['chat_manager'].create_chat(
            chat_manager_service_pb2.CreateChatRequest(
                chat_id=chat_id,
                username=username,
                language=language,
            ),
            metadata=(
                ('request-id', request_id), ('session-id', session_id),
            ),
        )
        return response

    async def get_chat(
        self,
        chat_id: int,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> chat_manager_service_pb2.Chat:
        response = await self.stubs['chat_manager'].get_chat(
            chat_manager_service_pb2.GetChatRequest(chat_id=chat_id),
            metadata=(
                ('request-id', request_id), ('session-id', session_id),
            ),
        )
        return response

    async def list_chats(
        self,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        banned_at_moment: Optional[str] = None,
    ) -> chat_manager_service_pb2.Chats:
        response = await self.stubs['chat_manager'].list_chats(
            chat_manager_service_pb2.ListChatsRequest(banned_at_moment=banned_at_moment),
            metadata=(
                ('request-id', request_id), ('session-id', session_id),
            ),
        )
        return response

    async def update_chat(
        self,
        chat_id: int,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        language: Optional[str] = None,
        is_system_messaging_enabled: Optional[bool] = None,
        is_discovery_enabled: Optional[bool] = None,
        is_connectome_enabled: Optional[bool] = None,
        ban_until: Optional[int] = None,
        ban_message: Optional[str] = None,
        is_admin: Optional[bool] = None,
    ) -> chat_manager_service_pb2.Chat:
        response = await self.stubs['chat_manager'].update_chat(
            chat_manager_service_pb2.UpdateChatRequest(
                chat_id=chat_id,
                language=language,
                is_system_messaging_enabled=is_system_messaging_enabled,
                is_discovery_enabled=is_discovery_enabled,
                is_connectome_enabled=is_connectome_enabled,
                ban_until=ban_until,
                ban_message=ban_message,
                is_admin=is_admin,
            ),
            metadata=(
                ('request-id', request_id), ('session-id', session_id),
            ),
        )
        return response

    async def get_profile(
        self,
        chat_id: int,
        starting_from: int = 0,
        last_n_documents: Optional[int] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> profile_service_pb2.GetProfileResponse:
        response = await self.stubs['profile'].get_profile(
            profile_service_pb2.GetProfileRequest(
                chat_id=chat_id,
                starting_from=starting_from,
                last_n_documents=last_n_documents,
            ),
            metadata=(
                ('request-id', request_id), ('session-id', session_id),
            ),
        )
        return response

    async def subscribe(
        self,
        chat_id: int,
        subscription_query: str,
        schedule: str,
        is_oneshot: Optional[bool] = None,
        is_downloadable: Optional[bool] = None,
        valid_until: Optional[int] = None,
        subscription_type: subscription_manager_service_pb2.Subscription.Type
        = subscription_manager_service_pb2.Subscription.Type.CUSTOM,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> subscription_manager_service_pb2.SubscribeResponse:
        response = await self.stubs['subscription_manager'].subscribe(
            subscription_manager_service_pb2.SubscribeRequest(
                chat_id=chat_id,
                subscription_query=subscription_query,
                schedule=schedule,
                is_oneshot=is_oneshot,
                is_downloadable=is_downloadable,
                valid_until=valid_until,
                subscription_type=subscription_type,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
            ),
        )
        return response

    async def get_single_chat_task(
        self,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> subscription_manager_service_pb2.GetSingleChatTaskResponse:
        response = await self.stubs['subscription_manager'].get_single_chat_task(
            subscription_manager_service_pb2.GetSingleChatTaskRequest(),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
            ),
        )
        return response

    async def reschedule_subscriptions(
        self,
        subscriptions_ids: dict,
        is_fired: bool = False,
        new_schedule: Optional[subscription_manager_service_pb2.NewSchedule] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> subscription_manager_service_pb2.RescheduleSubscriptionsResponse:
        response = await self.stubs['subscription_manager'].reschedule_subscriptions(
            subscription_manager_service_pb2.RescheduleSubscriptionsRequest(
                is_fired=is_fired,
                new_schedule=new_schedule,
                **subscriptions_ids,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
            ),
        )
        return response
