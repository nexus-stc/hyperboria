from typing import Optional

from aiokit import AioThing
from grpc.experimental.aio import insecure_channel
from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from nexus.hub.proto.delivery_service_pb2 import \
    StartDeliveryRequest as StartDeliveryRequestPb
from nexus.hub.proto.delivery_service_pb2 import \
    StartDeliveryResponse as StartDeliveryResponsePb
from nexus.hub.proto.delivery_service_pb2_grpc import DeliveryStub
from nexus.hub.proto.submitter_service_pb2 import \
    SubmitRequest as SubmitRequestPb
from nexus.hub.proto.submitter_service_pb2 import \
    SubmitResponse as SubmitResponsePb
from nexus.hub.proto.submitter_service_pb2_grpc import SubmitterStub
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb


class HubGrpcClient(AioThing):
    def __init__(
        self,
        base_url: str,
    ):
        super().__init__()
        self.channel = insecure_channel(base_url, [
            ('grpc.dns_min_time_between_resolutions_ms', 1000),
            ('grpc.initial_reconnect_backoff_ms', 1000),
            ('grpc.lb_policy_name', 'round_robin'),
            ('grpc.min_reconnect_backoff_ms', 1000),
            ('grpc.max_reconnect_backoff_ms', 2000),
        ])
        self.delivery_stub = DeliveryStub(self.channel)
        self.submitter_stub = SubmitterStub(self.channel)

    async def start(self):
        await self.channel.channel_ready()

    async def stop(self):
        await self.channel.close()

    async def start_delivery(
        self,
        typed_document_pb: TypedDocumentPb,
        chat: ChatPb,
        request_id: Optional[str],
        session_id: Optional[str],
    ) -> StartDeliveryResponsePb:
        return await self.delivery_stub.start_delivery(
            StartDeliveryRequestPb(
                typed_document=typed_document_pb,
                chat=chat,
            ),
            metadata=(('request-id', request_id), ('session-id', session_id))
        )

    async def submit(
        self,
        telegram_document: bytes,
        telegram_file_id: str,
        chat: ChatPb,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> SubmitResponsePb:
        return await self.submitter_stub.submit(
            SubmitRequestPb(
                telegram_document=telegram_document,
                telegram_file_id=telegram_file_id,
                chat=chat,
            ),
            metadata=(('request-id', request_id), ('session-id', session_id))
        )
