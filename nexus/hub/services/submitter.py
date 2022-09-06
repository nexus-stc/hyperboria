import asyncio
import hashlib
import logging
import re
import time
from difflib import SequenceMatcher

import orjson as json
from aiogrobid.exceptions import BadRequestError
from grpc import ServicerContext
from izihawa_utils.pb_to_json import MessageToDict
from library.aiogrpctools.base import aiogrpc_request_wrapper
from library.telegram.base import RequestContext
from library.telegram.common import close_button
from library.telegram.utils import safe_execution
from nexus.hub.exceptions import (
    FileTooBigError,
    UnavailableMetadataError,
    UnparsableDoiError,
)
from nexus.hub.proto import (
    submitter_service_pb2,
    submitter_service_pb2_grpc,
)
from nexus.models.proto import (
    operation_pb2,
    scimag_pb2,
    sharience_pb2,
    typed_document_pb2,
)
from nexus.pylon.pdftools import clean_metadata
from nexus.translations import t
from nexus.views.telegram.base_holder import ScimagHolder
from telethon.errors import ChatAdminRequiredError
from telethon.extensions import BinaryReader

from .base import (
    BaseHubService,
    ProcessedDocument,
)


async def operation_log(document_operation_pb):
    logging.getLogger('operation').info(msg=MessageToDict(document_operation_pb, preserving_proto_field_name=True))


class TelegramFile:
    def __init__(self, telegram_client, telegram_file):
        self.telegram_client = telegram_client
        self.telegram_file = telegram_file
        self.document = BinaryReader(telegram_file.document).tgread_object()

    @property
    def size(self):
        return self.document.size

    @property
    def message_id(self):
        return self.telegram_file.message_id

    @property
    def filename(self):
        return self.document.attributes[0].file_name

    async def read(self):
        return await self.telegram_client.download_document(
            document=self.document,
            file=bytes,
        )


class PlainFile:
    def __init__(self, plain_file):
        self.plain_file = plain_file

    @property
    def size(self):
        return len(self.plain_file.data)

    @property
    def message_id(self):
        return None

    @property
    def filename(self):
        return self.plain_file.filename

    async def read(self):
        return self.plain_file.data


def fuzzy_compare(a, b):
    a = re.sub(r'[^a-z\d]', '', a.lower())
    b = re.sub(r'[^a-z\d]', '', b.lower())
    return SequenceMatcher(None, a, b).ratio() > 0.9


class SubmitterService(submitter_service_pb2_grpc.SubmitterServicer, BaseHubService):
    async def start(self):
        submitter_service_pb2_grpc.add_SubmitterServicer_to_server(self, self.application.server)

    def wrap_request_file(self, request, request_context):
        match str(request.WhichOneof('file')):
            case 'plain':
                return PlainFile(request.plain)
            case 'telegram':
                return TelegramFile(self.application.telegram_clients[request_context.bot_name], request.telegram)
            case _:
                raise RuntimeError(f"Unknown file type {request.WhichOneof('file')}")

    async def retrieve_metadata(self, doi, title, session_id, request_context):
        if doi:
            meta_search_response = await self.application.meta_api_client.meta_search(
                index_aliases=['scimag', ],
                query=doi,
                collectors=[{'top_docs': {'limit': 1}}],
                session_id=session_id,
                request_id=request_context.request_id,
                user_id=str(request_context.chat.chat_id),
                query_tags=['submitter'],
            )
            scored_documents = meta_search_response.collector_outputs[0].top_docs.scored_documents
            if len(scored_documents) == 1:
                scimag_pb = scimag_pb2.Scimag(**json.loads(scored_documents[0].document))
                if title is not None and not fuzzy_compare(scimag_pb.title, title):
                    request_context.statbox(
                        action='mismatched_title',
                        doi=doi,
                        processed_title=title,
                        title=scimag_pb.title,
                    )
                    return None
                return scimag_pb

    @aiogrpc_request_wrapper(log=False)
    async def submit(
        self,
        request: submitter_service_pb2.SubmitRequest,
        context: ServicerContext,
        metadata: dict,
    ) -> submitter_service_pb2.SubmitResponse:
        session_id = metadata.get('session-id')
        request_context = RequestContext(
            bot_name=request.bot_name,
            chat=request.chat,
            request_id=metadata.get('request-id'),
        )
        request_context.add_default_fields(
            mode='submit',
            index_alias='scimag',
            session_id=metadata.get('session-id'),
            doi_hint=request.doi_hint,
            **self.get_default_service_fields(),
        )

        buttons = None if request_context.is_group_mode() else [close_button()]
        wrapped_file = self.wrap_request_file(request, request_context)

        if wrapped_file.size > 300 * 1024 * 1024:
            request_context.error_log(FileTooBigError(size=wrapped_file.size))
            request_context.statbox(action='file_too_big')
            async with safe_execution(error_log=request_context.error_log):
                await self.application.telegram_clients[request_context.bot_name].send_message(
                    request_context.chat.chat_id,
                    t('FILE_TOO_BIG_ERROR', request_context.chat.language),
                    buttons=buttons,
                    reply_to=request.reply_to,
                )
            return submitter_service_pb2.SubmitResponse()

        try:
            processing_message = await self.application.telegram_clients[request_context.bot_name].send_message(
                request_context.chat.chat_id,
                t("PROCESSING_PAPER", request_context.chat.language).format(filename=wrapped_file.filename),
                reply_to=request.reply_to,
            )
        except ChatAdminRequiredError:
            return submitter_service_pb2.SubmitResponse()

        try:
            file_data = await wrapped_file.read()
            if not request.skip_analysis:
                processed_document = await ProcessedDocument.setup(
                    file_data,
                    grobid_client=self.application.grobid_client,
                    request_context=request_context,
                )
            else:
                processed_document = ProcessedDocument({})

            if not processed_document.doi and not request.doi_hint:
                request_context.statbox(action='unparsable_doi')
                request_context.error_log(UnparsableDoiError())
                await self.application.telegram_clients[request_context.bot_name].send_message(
                    request_context.chat.chat_id,
                    t('UNPARSABLE_DOI_ERROR', request_context.chat.language).format(
                        filename=wrapped_file.filename,
                    ),
                    buttons=buttons,
                    reply_to=request.reply_to,
                )
                return submitter_service_pb2.SubmitResponse()

            scimag_pb = await self.retrieve_metadata(
                processed_document.doi,
                processed_document.title,
                session_id=session_id,
                request_context=request_context,
            )
            if not scimag_pb and request.doi_hint:
                scimag_pb = await self.retrieve_metadata(
                    request.doi_hint,
                    processed_document.title,
                    session_id=session_id,
                    request_context=request_context,
                )

            if not scimag_pb:
                request_context.statbox(action='unavailable_metadata')
                request_context.error_log(UnavailableMetadataError(doi=processed_document.doi))
                await self.application.telegram_clients[request_context.bot_name].send_message(
                    request_context.chat.chat_id,
                    t(
                        'UNAVAILABLE_METADATA_ERROR',
                        language=request_context.chat.language
                    ).format(doi=processed_document.doi or request.doi_hint),
                    buttons=buttons,
                    reply_to=request.reply_to,
                )
                return submitter_service_pb2.SubmitResponse()

            request_context.add_default_fields(doi=scimag_pb.doi, document_id=scimag_pb.id)
            try:
                file_data = clean_metadata(file_data, doi=scimag_pb.doi)
                request_context.statbox(action='cleaned', len=len(file_data))
            except ValueError as e:
                request_context.error_log(e)
            uploaded_message = await self.send_file(
                document_holder=ScimagHolder(scimag_pb),
                file=file_data,
                request_context=request_context,
                session_id=session_id,
                voting=False,
            )

            if processed_document:
                sharience_pb = sharience_pb2.Sharience(
                    abstract=processed_document.abstract or '',
                    content=processed_document.body or '',
                    parent_id=scimag_pb.id,
                    uploader_id=request.uploader_id or request_context.chat.chat_id,
                    updated_at=int(time.time()),
                    md5=hashlib.md5(file_data).hexdigest(),
                    filesize=wrapped_file.size,
                    ipfs_multihashes=await self.get_ipfs_hashes(file=file_data),
                )
                update_sharience_pb = operation_pb2.DocumentOperation(
                    update_document=operation_pb2.UpdateDocument(
                        full_text_index=True,
                        typed_document=typed_document_pb2.TypedDocument(sharience=sharience_pb),
                    ),
                )
                await operation_log(update_sharience_pb)

                new_fields = self.set_fields_from_processed(scimag_pb, processed_document)
                if new_fields:
                    update_scimag_pb = operation_pb2.DocumentOperation(
                        update_document=operation_pb2.UpdateDocument(
                            full_text_index=True,
                            typed_document=typed_document_pb2.TypedDocument(scimag=scimag_pb),
                            fields=new_fields
                        ),
                    )
                    await operation_log(update_scimag_pb)
            store_telegram_file_id_operation_pb = operation_pb2.DocumentOperation(
                store_telegram_file_id=operation_pb2.StoreTelegramFileId(
                    document_id=scimag_pb.id,
                    telegram_file_id=uploaded_message.file.id,
                    bot_name=request_context.bot_name,
                ),
            )
            await operation_log(store_telegram_file_id_operation_pb)
            request_context.statbox(action='successfully_stored')

            if wrapped_file.message_id:
                async with safe_execution(error_log=request_context.error_log, level=logging.DEBUG):
                    await self.application.telegram_clients[request_context.bot_name].delete_messages(
                        request_context.chat.chat_id,
                        wrapped_file.message_id,
                    )
            await self.found_item(bot_name=request_context.bot_name, doi=scimag_pb.doi)
        finally:
            await processing_message.delete()
        return submitter_service_pb2.SubmitResponse()
