import asyncio
import json
import logging
from contextlib import suppress
from timeit import default_timer

from aiokit import AioThing
from cachetools import TTLCache
from grpc import StatusCode
from izihawa_utils.exceptions import NeedRetryError
from izihawa_utils.pb_to_json import MessageToDict
from izihawa_utils.text import camel_to_snake
from library.aiogrpctools.base import (
    BaseService,
    aiogrpc_request_wrapper,
)
from nexus.meta_api.proto.search_service_pb2 import \
    ScoredDocument as ScoredDocumentPb
from nexus.meta_api.proto.search_service_pb2 import \
    SearchResponse as SearchResponsePb
from nexus.meta_api.proto.search_service_pb2_grpc import (
    SearchServicer,
    add_SearchServicer_to_server,
)
from nexus.meta_api.query_extensions import (
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


class ClassicSearcher(BaseService):
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

    async def processed_query_hook(self, processed_query, context):
        if processed_query['class'] == QueryClass.URL:
            await context.abort(StatusCode.INVALID_ARGUMENT, 'url_query_error')
        return processed_query

    def merge_search_responses(self, search_responses):
        if not search_responses:
            return
        elif len(search_responses) == 1:
            return search_responses[0]
        return SearchResponsePb(
            scored_documents=[
                scored_document
                for search_response in search_responses
                for scored_document in search_response.scored_documents
            ],
            has_next=any([search_response.has_next for search_response in search_responses]),
        )

    def cast_search_response(self, name, search_response):
        scored_documents_pb = []
        for scored_document in search_response['scored_documents']:
            document = json.loads(scored_document['document'])
            for field in document:
                if field in {'authors', 'ipfs_multihashes', 'isbns', 'issns', 'references', 'tags'}:
                    continue
                document[field] = document[field][0]

            original_id = (
                document.get('original_id')
                or document['id']
            )
            download_stats = self.stat_provider.get_download_stats(original_id)
            if download_stats and download_stats.downloads_count:
                document['downloads_count'] = download_stats.downloads_count

            scored_documents_pb.append(ScoredDocumentPb(
                position=scored_document['position'],
                score=scored_document['score'],
                typed_document=TypedDocumentPb(
                    **{name: pb_registry[name](**document)},
                )
            ))
        return SearchResponsePb(
            scored_documents=scored_documents_pb,
            has_next=search_response['has_next'],
        )

    @aiogrpc_request_wrapper()
    async def search(self, request, context, metadata):
        start = default_timer()
        processed_query = None
        cache_hit = True
        page_size = request.page_size or 5
        index_aliases = tuple(sorted([index_alias for index_alias in request.index_aliases]))
        user_id = metadata['user-id']

        if (
            (user_id, request.language, index_aliases, request.query) not in self.query_cache
            or len(self.query_cache[(user_id, request.language, index_aliases, request.query)].scored_documents) == 0
        ):
            cache_hit = False
            query = despace_full(request.query)
            processed_query = self.query_processor.process(query, request.language)
            processed_query = await self.processed_query_hook(processed_query, context)

            with suppress(RetryError):
                async for attempt in AsyncRetrying(
                    retry=retry_if_exception_type(NeedRetryError),
                    wait=wait_fixed(15),
                    stop=stop_after_attempt(2)
                ):
                    with attempt:
                        requests = []
                        for index_alias in index_aliases:
                            requests.append(
                                self.summa_client.search(
                                    index_alias=index_alias,
                                    query=processed_query['query'],
                                    offset=0,
                                    limit=self.page_sizes[index_alias],
                                    request_id=metadata['request-id'],
                                )
                            )
                        search_responses = [
                            MessageToDict(
                                search_response,
                                preserving_proto_field_name=True,
                                including_default_value_fields=True,
                            ) for search_response in await asyncio.gather(*requests)
                        ]
                        search_responses_pb = [
                            self.cast_search_response(name, search_response)
                            for (name, search_response) in zip(index_aliases, search_responses)
                        ]
                        search_response_pb = self.merge_search_responses(search_responses_pb)

                        if len(search_response_pb.scored_documents) == 0 and processed_query['class'] == QueryClass.DOI:
                            if attempt.retry_state.attempt_number == 1:
                                await self.request_doi_delivery(doi=processed_query['doi'])
                            raise NeedRetryError()

            rescored_documents = await self.rescorer.rescore(
                scored_documents=search_response_pb.scored_documents,
                query=query,
                session_id=metadata['session-id'],
                language=request.language,
            )
            search_response_pb = SearchResponsePb(
                scored_documents=rescored_documents,
                has_next=search_response_pb.has_next,
            )
            self.query_cache[(user_id, request.language, index_aliases, request.query)] = search_response_pb

        logging.getLogger('query').info({
            'action': 'request',
            'cache_hit': cache_hit,
            'duration': default_timer() - start,
            'index_aliases': index_aliases,
            'mode': 'search',
            'page': request.page,
            'page_size': page_size,
            'processed_query': processed_query['query'] if processed_query else None,
            'query': request.query,
            'query_class': processed_query['class'].value if processed_query else None,
            'request_id': metadata['request-id'],
            'session_id': metadata['session-id'],
            'user_id': user_id,
        })

        scored_documents = self.query_cache[(user_id, request.language, index_aliases, request.query)].scored_documents
        left_offset = request.page * page_size
        right_offset = left_offset + page_size
        has_next = len(scored_documents) > right_offset

        search_response_pb = SearchResponsePb(
            scored_documents=scored_documents[left_offset:right_offset],
            has_next=has_next,
        )

        return search_response_pb

    async def request_doi_delivery(self, doi):
        document_operation = DocumentOperationPb(
            update_document=UpdateDocumentPb(
                commit=True,
                reindex=True,
                should_fill_from_external_source=True,
                typed_document=TypedDocumentPb(scimag=ScimagPb(doi=doi)),
            ),
        )
        self.operation_logger.info(MessageToDict(document_operation, preserving_proto_field_name=True))


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
