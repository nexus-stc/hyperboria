from typing import Optional

from aiogrpcclient import BaseGrpcClient
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


class HubGrpcClient(BaseGrpcClient):
    stub_clses = {
        'delivery': DeliveryStub,
        'submitter': SubmitterStub,
    }

    async def start_delivery(
        self,
        typed_document_pb: TypedDocumentPb,
        chat: ChatPb,
        bot_name: str,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> StartDeliveryResponsePb:
        return await self.stubs['delivery'].start_delivery(
            StartDeliveryRequestPb(
                typed_document=typed_document_pb,
                chat=chat,
                bot_name=bot_name,
            ),
            metadata=(('request-id', request_id), ('session-id', session_id))
        )

    async def submit(
        self,
        telegram_document: bytes,
        telegram_file_id: str,
        chat: ChatPb,
        bot_name: str,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> SubmitResponsePb:
        return await self.stubs['submitter'].submit(
            SubmitRequestPb(
                telegram_document=telegram_document,
                telegram_file_id=telegram_file_id,
                chat=chat,
                bot_name=bot_name,
            ),
            metadata=(('request-id', request_id), ('session-id', session_id))
        )
