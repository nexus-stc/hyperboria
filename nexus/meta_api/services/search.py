import asyncio
import logging
from contextlib import suppress
from timeit import default_timer

from aiokit import AioThing
from cachetools import TTLCache
from google.protobuf.json_format import MessageToDict
from grpc import StatusCode
from izihawa_utils.exceptions import NeedRetryError
from izihawa_utils.text import camel_to_snake
from library.aiogrpctools.base import aiogrpc_request_wrapper
from nexus.meta_api.proto.search_service_pb2 import \
    ScoredDocument as ScoredDocumentPb
from nexus.meta_api.proto.search_service_pb2 import \
    SearchResponse as SearchResponsePb
from nexus.meta_api.proto.search_service_pb2_grpc import (
    SearchServicer,
    add_SearchServicer_to_server,
)
from nexus.meta_api.query_extensionner import (
    ClassicQueryProcessor,
    QueryClass,
)
from nexus.meta_api.rescorers import ClassicRescorer
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.operation_pb2 import UpdateDocument as UpdateDocumentPb
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from nexus.nlptools.utils import despace_full
from nexus.views.telegram.registry import pb_registry
from tenacity import (
    AsyncRetrying,
    RetryError,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)

from .base import BaseService


class Searcher(BaseService):
    page_sizes = {
        'scimag': 100,
        'scitech': 100,
    }

    def __init__(self, summa_client, query_processor, rescorer, stat_provider):
        super().__init__(service_name='meta_api')
        self.summa_client = summa_client

        self.operation_logger = logging.getLogger('operation')
        self.class_name = camel_to_snake(self.__class__.__name__)

        self.query_cache = TTLCache(maxsize=1024 * 4, ttl=300)
        self.query_processor = query_processor
        self.rescorer = rescorer
        self.stat_provider = stat_provider

    async def processed_response_hook(self, processor_response, context):
        return processor_response

    async def post_search_hook(self, search_response, processor_response, request, context,
                               metadata, retry_state):
        return search_response

    def merge_search_responses(self, search_responses):
        if not search_responses:
            return
        elif len(search_responses) == 1:
            return search_responses[0]
        return dict(
            scored_documents=[
                scored_document
                for search_response in search_responses
                for scored_document in search_response['scored_documents']
            ],
            has_next=any([search_response['has_next'] for search_response in search_responses]),
        )

    def cast_search_response(self, search_response):
        scored_documents_pb = []
        for scored_document in search_response['scored_documents']:
            document_pb = pb_registry[scored_document['schema']](**scored_document['document'])
            scored_documents_pb.append(ScoredDocumentPb(
                position=scored_document['position'],
                score=scored_document['score'],
                typed_document=TypedDocumentPb(
                    **{scored_document['schema']: document_pb},
                )
            ))
        return SearchResponsePb(
            scored_documents=scored_documents_pb,
            has_next=search_response['has_next'],
        )

    @aiogrpc_request_wrapper()
    async def search(self, request, context, metadata):
        start = default_timer()
        processor_response = None
        cache_hit = True
        page_size = request.page_size or 5

        if (
            (request.user_id, request.language, request.query) not in self.query_cache
            or len(self.query_cache[(request.user_id, request.language, request.query)].scored_documents) == 0
        ):
            cache_hit = False
            query = despace_full(request.query)
            processor_response = self.query_processor.process(query, request.language)
            processor_response = await self.processed_response_hook(processor_response, context)

            with suppress(RetryError):
                async for attempt in AsyncRetrying(
                    retry=retry_if_exception_type(NeedRetryError),
                    wait=wait_fixed(10),
                    stop=stop_after_attempt(3)
                ):
                    with attempt:
                        requests = []
                        for schema in request.schemas:
                            requests.append(
                                self.summa_client.search(
                                    schema=schema,
                                    query=processor_response['query'],
                                    page=0,
                                    page_size=self.page_sizes[schema],
                                    request_id=metadata['request-id'],
                                )
                            )
                        search_response = self.merge_search_responses(await asyncio.gather(*requests))
                        search_response = await self.post_search_hook(
                            search_response,
                            processor_response=processor_response,
                            request=request,
                            context=context,
                            metadata=metadata,
                            retry_state=attempt.retry_state
                        )

            rescored_documents = await self.rescorer.rescore(
                scored_documents=search_response['scored_documents'],
                query=query,
                session_id=request.session_id,
                language=request.language,
            )
            search_response['scored_documents'] = rescored_documents
            search_response_pb = self.cast_search_response(search_response)
            self.query_cache[(request.user_id, request.language, request.query)] = search_response_pb

        logging.getLogger('query').info({
            'action': 'request',
            'cache_hit': cache_hit,
            'duration': default_timer() - start,
            'mode': 'search',
            'page': request.page,
            'page_size': page_size,
            'processed_query': processor_response['query'] if processor_response else None,
            'query': request.query,
            'query_class': processor_response['class'].value if processor_response else None,
            'request_id': metadata['request-id'],
            'schemas': [schema for schema in request.schemas],
            'session_id': request.session_id,
            'user_id': request.user_id,
        })

        scored_documents = self.query_cache[(request.user_id, request.language, request.query)].scored_documents
        left_offset = request.page * page_size
        right_offset = left_offset + page_size
        has_next = len(scored_documents) > right_offset

        search_response_pb = SearchResponsePb(
            scored_documents=scored_documents[left_offset:right_offset],
            has_next=has_next,
        )

        return search_response_pb


class ClassicSearcher(Searcher):
    async def processed_response_hook(self, processor_response, context):
        if processor_response['class'] == QueryClass.URL:
            await context.abort(StatusCode.INVALID_ARGUMENT, 'url_query_error')
        return processor_response

    async def post_search_hook(self, search_response, processor_response, request, context, metadata,
                               retry_state):
        if len(search_response['scored_documents']) == 0 and processor_response['class'] == QueryClass.DOI:
            if retry_state.attempt_number == 1:
                await self.request_doi_delivery(doi=processor_response['doi'])
            raise NeedRetryError()
        for scored_document in search_response['scored_documents']:
            original_id = (
                scored_document['document'].get('original_id')
                or scored_document['document']['id']
            )
            download_stats = self.stat_provider.get_download_stats(original_id)
            if download_stats and download_stats.downloads_count:
                scored_document['document']['downloads_count'] = download_stats.downloads_count
        return search_response

    async def request_doi_delivery(self, doi):
        document_operation = DocumentOperationPb(
            update_document=UpdateDocumentPb(
                commit=True,
                reindex=True,
                should_fill_from_external_source=True,
                typed_document=TypedDocumentPb(scimag=ScimagPb(doi=doi)),
            ),
        )
        self.operation_logger.info(MessageToDict(document_operation))


class SearchService(SearchServicer, AioThing):
    def __init__(self, server, summa_client, stat_provider, learn_logger=None):
        super().__init__()
        self.server = server
        self.searcher = ClassicSearcher(
            summa_client=summa_client,
            query_processor=ClassicQueryProcessor(),
            rescorer=ClassicRescorer(
                learn_logger=learn_logger,
            ),
            stat_provider=stat_provider,
        )
        self.starts.append(self.searcher)

    async def start(self):
        add_SearchServicer_to_server(self, self.server)

    async def search(self, request, context):
        return await self.searcher.search(request, context)
