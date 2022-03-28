import asyncio
import hashlib
import logging
import time

from aiogrobid import GrobidClient
from aiogrobid.exceptions import BadRequestError
from grpc import (
    Server,
    ServicerContext,
)
from izihawa_utils.pb_to_json import MessageToDict
from library.aiogrpctools.base import aiogrpc_request_wrapper
from library.telegram.base import RequestContext
from nexus.hub.exceptions import (
    FileTooBigError,
    UnavailableMetadataError,
    UnparsableDoiError,
)
from nexus.hub.proto.submitter_service_pb2 import \
    SubmitRequest as SubmitRequestPb
from nexus.hub.proto.submitter_service_pb2 import \
    SubmitResponse as SubmitResponsePb
from nexus.hub.proto.submitter_service_pb2_grpc import (
    SubmitterServicer,
    add_SubmitterServicer_to_server,
)
from nexus.hub.user_manager import UserManager
from nexus.meta_api.aioclient import MetaApiGrpcClient
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.operation_pb2 import \
    StoreTelegramFileId as StoreTelegramFileIdPb
from nexus.models.proto.operation_pb2 import UpdateDocument as UpdateDocumentPb
from nexus.models.proto.sharience_pb2 import Sharience as ShariencePb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from nexus.translations import t
from nexus.views.telegram.common import close_button
from nexus.views.telegram.scimag import ScimagView
from telethon.extensions import BinaryReader

from .base import BaseHubService


async def operation_log(document_operation_pb):
    logging.getLogger('operation').info(msg=MessageToDict(document_operation_pb, preserving_proto_field_name=True))


class SubmitterService(SubmitterServicer, BaseHubService):
    def __init__(
        self,
        server: Server,
        service_name: str,
        grobid_config: dict,
        ipfs_config: dict,
        meta_api_config: dict,
        telegram_clients,
    ):
        super().__init__(
            service_name=service_name,
            ipfs_config=ipfs_config,
            telegram_clients=telegram_clients,
        )
        self.server = server
        self.grobid_client = GrobidClient(base_url=grobid_config['url'])
        self.meta_api_client = MetaApiGrpcClient(endpoint=meta_api_config['endpoint'])
        self.telegram_clients = telegram_clients
        self.user_manager = UserManager()
        self.waits.extend([self.grobid_client, self.meta_api_client])

    async def start(self):
        await super().start()
        add_SubmitterServicer_to_server(self, self.server)

    async def stop(self):
        await self.ipfs_client.close()

    @aiogrpc_request_wrapper(log=False)
    async def submit(
        self,
        request: SubmitRequestPb,
        context: ServicerContext,
        metadata: dict,
    ) -> SubmitResponsePb:
        session_id = metadata.get('session-id')
        request_context = RequestContext(
            bot_name=request.bot_name,
            chat=request.chat,
            request_id=metadata.get('request-id'),
        )
        request_context.add_default_fields(
            mode='submit',
            session_id=metadata.get('session-id'),
            **self.get_default_service_fields(),
        )

        document = BinaryReader(request.telegram_document).tgread_object()
        if document.size > 20 * 1024 * 1024:
            request_context.error_log(FileTooBigError(size=document.size))
            request_context.statbox(action='file_too_big')
            await self.telegram_clients[request_context.bot_name].send_message(
                request_context.chat.chat_id,
                t('FILE_TOO_BIG_ERROR', language=request_context.chat.language),
                buttons=[close_button()],
            )
            return SubmitResponsePb()
        processing_message = await self.telegram_clients[request_context.bot_name].send_message(
            request_context.chat.chat_id,
            t("PROCESSING_PAPER", language=request_context.chat.language).format(
                filename=document.attributes[0].file_name,
            ),
        )
        try:
            file = await self.telegram_clients[request_context.bot_name].download_document(document=document, file=bytes)
            try:
                processed_document = await self.grobid_client.process_fulltext_document(pdf_file=file)
            except BadRequestError as e:
                request_context.statbox(action='unparsable_document')
                request_context.error_log(e)
                await self.telegram_clients[request_context.bot_name].send_message(
                    request_context.chat.chat_id,
                    t('UNPARSABLE_DOCUMENT_ERROR', language=request_context.chat.language).format(
                        filename=document.attributes[0].file_name,
                    ),
                    buttons=[close_button()],
                )
                return SubmitResponsePb()

            if not processed_document.get('doi'):
                request_context.statbox(action='unparsable_doi')
                request_context.error_log(UnparsableDoiError())
                await self.telegram_clients[request_context.bot_name].send_message(
                    request_context.chat.chat_id,
                    t('UNPARSABLE_DOI_ERROR', language=request_context.chat.language).format(
                        filename=document.attributes[0].file_name,
                    ),
                    buttons=[close_button()],
                )
                return SubmitResponsePb()

            search_response_pb = await self.meta_api_client.search(
                names=('scimag',),
                query=processed_document['doi'],
                page=0,
                page_size=1,
                request_id=request_context.request_id,
                session_id=session_id,
                user_id=str(request_context.chat.chat_id),
                language=request_context.chat.language,
            )

            if len(search_response_pb.scored_documents) == 0:
                request_context.statbox(action='unavailable_metadata')
                request_context.error_log(UnavailableMetadataError(doi=processed_document['doi']))
                await self.telegram_clients[request_context.bot_name].send_message(
                    request_context.chat.chat_id,
                    t(
                        'UNAVAILABLE_METADATA_ERROR',
                        language=request_context.chat.language
                    ).format(doi=processed_document['doi']),
                    buttons=[close_button()],
                )
                return SubmitResponsePb()

            document_view = ScimagView(search_response_pb.scored_documents[0].typed_document.scimag)
            uploaded_message = await self.send_file(
                document_view=document_view,
                file=file,
                request_context=request_context,
                session_id=session_id,
                voting=False,
            )
        finally:
            await processing_message.delete()

        update_document_operation_pb = DocumentOperationPb(
            update_document=UpdateDocumentPb(
                typed_document=TypedDocumentPb(sharience=ShariencePb(
                    parent_id=document_view.id,
                    uploader_id=request_context.chat.chat_id,
                    updated_at=int(time.time()),
                    md5=hashlib.md5(file).hexdigest(),
                    filesize=document.size,
                    ipfs_multihashes=await self.get_ipfs_hashes(file=file),
                )),
            ),
        )
        store_telegram_file_id_operation_pb = DocumentOperationPb(
            store_telegram_file_id=StoreTelegramFileIdPb(
                document_id=document_view.id,
                telegram_file_id=uploaded_message.file.id,
                bot_name=request_context.bot_name,
            ),
        )
        request_context.statbox(
            action='success',
            document_id=document_view.id,
            schema='scimag',
        )
        await asyncio.gather(
            operation_log(update_document_operation_pb),
            operation_log(store_telegram_file_id_operation_pb),
        )
        return SubmitResponsePb()
