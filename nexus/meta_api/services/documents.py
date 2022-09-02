import logging

from grpc import StatusCode
from library.aiogrpctools.base import aiogrpc_request_wrapper
from nexus.meta_api.proto.documents_service_pb2_grpc import (
    DocumentsServicer,
    add_DocumentsServicer_to_server,
)
from nexus.meta_api.services.base import BaseService
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from summa.proto import search_service_pb2


class DocumentsService(DocumentsServicer, BaseService):
    def __init__(self, application, query_preprocessor, query_transformers, summa_client, stat_provider, learn_logger=None):
        super().__init__(
            application=application,
            stat_provider=stat_provider,
            summa_client=summa_client,
        )
        self.stat_provider = stat_provider
        self.query_preprocessor = query_preprocessor
        self.query_transformers = query_transformers
        self.learn_logger = learn_logger

    async def start(self):
        add_DocumentsServicer_to_server(self, self.application.server)

    async def get_document(self, index_alias, document_id, context, request_id, session_id):
        search_response = await self.summa_client.search(
            index_alias=index_alias,
            query={'term': {'field': 'id', 'value': str(document_id)}},
            collectors=search_service_pb2.Collector(
                top_docs=search_service_pb2.TopDocsCollector(limit=1)
            ),
            request_id=request_id,
            session_id=session_id,
        )
        scored_documents = self.cast_top_docs_collector(
            scored_documents=search_response.collector_outputs[0].top_docs.scored_documents,
        )
        if scored_documents:
            return scored_documents[0].typed_document
        else:
            return await context.abort(StatusCode.NOT_FOUND, 'not_found')

    @aiogrpc_request_wrapper(log=False)
    async def get(self, request, context, metadata) -> TypedDocumentPb:
        typed_document_pb = await self.get_document(
            index_alias=request.index_alias,
            document_id=request.document_id,
            context=context,
            request_id=metadata['request-id'],
            session_id=metadata['session-id'],
        )

        document_pb = getattr(typed_document_pb, typed_document_pb.WhichOneof('document'))

        if hasattr(document_pb, 'original_id') and document_pb.original_id:
            original_document_pb = await self.get_document(
                index_alias=request.index_alias,
                document_id=document_pb.original_id,
                context=context,
                request_id=metadata['request-id'],
                session_id=metadata['session-id'],
            )
            for to_remove in ('doi', 'fiction_id', 'filesize', 'libgen_id',):
                original_document_pb.ClearField(to_remove)
            original_document_pb.MergeFrom(document_pb)
            document_pb = original_document_pb

        logging.getLogger('query').info({
            'action': 'get',
            'cache_hit': False,
            'id': document_pb.id,
            'index_alias': request.index_alias,
            'mode': 'get',
            'position': request.position,
            'request_id': metadata['request-id'],
            'session_id': metadata['session-id'],
            'user_id': metadata['user-id'],
        })

        return typed_document_pb
