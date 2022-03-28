import json
import logging
import time

from grpc import StatusCode
from library.aiogrpctools.base import (
    BaseService,
    aiogrpc_request_wrapper,
)
from nexus.meta_api.proto.documents_service_pb2 import \
    RollResponse as RollResponsePb
from nexus.meta_api.proto.documents_service_pb2 import \
    TopMissedResponse as TopMissedResponsePb
from nexus.meta_api.proto.documents_service_pb2_grpc import (
    DocumentsServicer,
    add_DocumentsServicer_to_server,
)
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from nexus.views.telegram.registry import pb_registry


class DocumentsService(DocumentsServicer, BaseService):
    def __init__(self, server, summa_client, data_provider, stat_provider, learn_logger=None):
        super().__init__(service_name='meta_api')
        self.server = server
        self.summa_client = summa_client
        self.stat_provider = stat_provider
        self.data_provider = data_provider
        self.learn_logger = learn_logger

    async def get_document(self, index_alias, document_id, request_id, context):
        search_response = await self.summa_client.search(
            index_alias=index_alias,
            query=f'id:{document_id}',
            offset=0,
            limit=1,
            request_id=request_id,
        )

        if len(search_response.scored_documents) == 0:
            await context.abort(StatusCode.NOT_FOUND, 'not_found')

        loaded = json.loads(search_response.scored_documents[0].document)
        for field in loaded:
            if field in {'authors', 'ipfs_multihashes', 'isbns', 'issns', 'references', 'tags'}:
                continue
            loaded[field] = loaded[field][0]
        return loaded

    def copy_document(self, source, target):
        for key in source:
            target[key] = source[key]

    async def start(self):
        add_DocumentsServicer_to_server(self, self.server)

    @aiogrpc_request_wrapper()
    async def get(self, request, context, metadata) -> TypedDocumentPb:
        document = await self.get_document(request.index_alias, request.document_id, metadata['request-id'], context)
        if document.get('original_id'):
            original_document = await self.get_document(
                index_alias=request.index_alias,
                document_id=document['original_id'],
                request_id=metadata['request-id'],
                context=context,
            )
            for to_remove in ('doi', 'fiction_id', 'filesize', 'libgen_id',):
                original_document.pop(to_remove, None)
            document = {**original_document, **document}

        document_data = await self.data_provider.get(request.document_id)
        download_stats = self.stat_provider.get_download_stats(request.document_id)

        if self.learn_logger:
            self.learn_logger.info({
                'action': 'get',
                'document_id': document['id'],
                'index_alias': request.index_alias,
                'session_id': metadata['session-id'],
                'unixtime': time.time(),
            })

        logging.getLogger('query').info({
            'action': 'get',
            'cache_hit': False,
            'id': document['id'],
            'index_alias': request.index_alias,
            'mode': 'get',
            'position': request.position,
            'request_id': metadata['request-id'],
            'session_id': metadata['session-id'],
            'user_id': metadata['user-id'],
        })

        document_pb = pb_registry[request.index_alias](**document)
        if document_data:
            del document_pb.ipfs_multihashes[:]
            document_pb.ipfs_multihashes.extend(document_data.ipfs_multihashes)
        if download_stats and download_stats.downloads_count:
            document_pb.downloads_count = download_stats.downloads_count

        return TypedDocumentPb(
            **{request.index_alias: document_pb},
        )

    @aiogrpc_request_wrapper()
    async def roll(self, request, context, metadata):
        random_id = await self.data_provider.random_id(request.language)

        logging.getLogger('query').info({
            'action': 'roll',
            'cache_hit': False,
            'id': random_id,
            'mode': 'roll',
            'request_id': metadata['request-id'],
            'session_id': metadata['session-id'],
            'user_id': metadata['user-id'],
        })

        return RollResponsePb(document_id=random_id)

    @aiogrpc_request_wrapper()
    async def top_missed(self, request, context, metadata):
        document_ids = self.stat_provider.get_top_missed_stats()
        offset = request.page * request.page_size
        limit = request.page_size
        document_ids = document_ids[offset:offset + limit]
        document_ids = map(lambda document_id: f'id:{document_id}', document_ids)
        document_ids = ' OR '.join(document_ids)

        search_response = await self.summa_client.search(
            index_alias='scimag',
            query=document_ids,
            limit=limit,
            request_id=metadata['request-id'],
        )

        if len(search_response.scored_documents) == 0:
            await context.abort(StatusCode.NOT_FOUND, 'not_found')

        documents = list(map(
            lambda document: TypedDocumentPb(scimag=ScimagPb(**json.loads(document.typed_document.scimag))),
            search_response.scored_documents,
        ))

        return TopMissedResponsePb(typed_documents=documents)
