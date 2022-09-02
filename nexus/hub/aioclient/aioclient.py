from typing import (
    Optional,
    Union,
)

from aiogrpcclient import BaseGrpcClient
from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from nexus.hub.proto import (
    delivery_service_pb2,
    delivery_service_pb2_grpc,
    submitter_service_pb2,
    submitter_service_pb2_grpc,
)
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb


class HubGrpcClient(BaseGrpcClient):
    stub_clses = {
        'delivery': delivery_service_pb2_grpc.DeliveryStub,
        'submitter': submitter_service_pb2_grpc.SubmitterStub,
    }

    async def get_availability_data(
        self,
        document_id: int,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> delivery_service_pb2.GetAvailabilityDataResponse:
        return await self.stubs['delivery'].get_availability_data(
            delivery_service_pb2.GetAvailabilityDataRequest(
                document_id=document_id,
            ),
            metadata=(('request-id', request_id), ('session-id', session_id))
        )

    async def start_delivery(
        self,
        typed_document_pb: TypedDocumentPb,
        chat: ChatPb,
        bot_name: str,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> delivery_service_pb2.StartDeliveryResponse:
        return await self.stubs['delivery'].start_delivery(
            delivery_service_pb2.StartDeliveryRequest(
                typed_document=typed_document_pb,
                chat=chat,
                bot_name=bot_name,
            ),
            metadata=(('request-id', request_id), ('session-id', session_id))
        )

    async def submit(
        self,
        file: Union[submitter_service_pb2.PlainFile, submitter_service_pb2.TelegramFile],
        chat: ChatPb,
        bot_name: str,
        reply_to: Optional[int] = None,
        doi_hint: Optional[str] = None,
        doi_hint_priority: bool = False,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        uploader_id: Optional[int] = None
    ) -> submitter_service_pb2.SubmitResponse:
        request = submitter_service_pb2.SubmitRequest(
            chat=chat,
            bot_name=bot_name,
            reply_to=reply_to,
            doi_hint=doi_hint,
            doi_hint_priority=doi_hint_priority,
            uploader_id=uploader_id,
        )
        if isinstance(file, submitter_service_pb2.PlainFile):
            request.plain.CopyFrom(file)
        if isinstance(file, submitter_service_pb2.TelegramFile):
            request.telegram.CopyFrom(file)
        return await self.stubs['submitter'].submit(request, metadata=(('request-id', request_id), ('session-id', session_id)))
