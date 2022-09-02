import asyncio
import dataclasses
import logging
import sys
from contextlib import suppress
from datetime import timedelta
from timeit import default_timer
from typing import (
    Dict,
    List,
    Optional,
    Union,
)

import orjson as json
from aiosumma.eval_scorer_builder import EvalScorerBuilder
from aiosumma.parser.errors import ParseError
from aiosumma.processor import ProcessedQuery
from cachetools import TTLCache
from grpc import StatusCode
from izihawa_utils.exceptions import NeedRetryError
from izihawa_utils.pb_to_json import MessageToDict
from library.aiogrpctools.base import aiogrpc_request_wrapper
from nexus.meta_api.mergers import (
    AggregationMerger,
    CountMerger,
    ReservoirSamplingMerger,
    TopDocsMerger,
)
from nexus.meta_api.proto import search_service_pb2 as meta_search_service_pb2
from nexus.meta_api.proto.search_service_pb2_grpc import (
    SearchServicer,
    add_SearchServicer_to_server,
)
from nexus.meta_api.services.base import BaseService
from nexus.models.proto import (
    operation_pb2,
    scimag_pb2,
    typed_document_pb2,
)
from summa.proto import search_service_pb2
from tenacity import (
    AsyncRetrying,
    RetryError,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)


def to_bool(b: Union[str, None, bool, int]):
    if isinstance(b, str):
        return b == '1'
    if b is None:
        return False
    return bool(b)


@dataclasses.dataclass
class SearchRequest:
    index_alias: str
    query: ProcessedQuery
    collectors: List[Dict]

    def cache_key(self):
        return (
            self.index_alias,
            str(self.query),
            json.dumps(
                [MessageToDict(collector, preserving_proto_field_name=True) for collector in self.collectors],
                option=json.OPT_SORT_KEYS,
            ),
        )


class SearchService(SearchServicer, BaseService):
    snippets = {
        'scimag': {
            'title': 1024,
            'abstract': 100,
        },
        'scitech': {
            'title': 1024,
            'description': 100,
        }
    }

    def __init__(self, application, stat_provider, summa_client, query_preprocessor, query_transformers, learn_logger=None):
        super().__init__(
            application=application,
            stat_provider=stat_provider,
            summa_client=summa_client,
        )
        self.query_cache = TTLCache(maxsize=1024 * 4, ttl=300)
        self.query_preprocessor = query_preprocessor
        self.query_transformers = query_transformers
        self.learn_logger = learn_logger

    async def start(self):
        add_SearchServicer_to_server(self, self.application.server)

    def merge_search_responses(self, search_responses, collector_descriptors: List[str]):
        collector_outputs = []
        for i, collector_descriptor in enumerate(collector_descriptors):
            match collector_descriptor:
                case 'aggregation':
                    merger = AggregationMerger([
                        search_response.collector_outputs[i].aggregation
                        for search_response in search_responses if search_response.collector_outputs
                    ])
                case 'count':
                    merger = CountMerger([
                        search_response.collector_outputs[i].count
                        for search_response in search_responses if search_response.collector_outputs
                    ])
                case 'top_docs':
                    merger = TopDocsMerger([
                        search_response.collector_outputs[i].top_docs
                        for search_response in search_responses if search_response.collector_outputs
                    ])
                case 'reservoir_sampling':
                    merger = ReservoirSamplingMerger([
                        search_response.collector_outputs[i].reservoir_sampling
                        for search_response in search_responses if search_response.collector_outputs
                    ])
                case _:
                    raise RuntimeError("Unsupported collector")
            collector_outputs.append(merger.merge())
        return meta_search_service_pb2.MetaSearchResponse(collector_outputs=collector_outputs)

    async def check_if_need_new_documents_by_dois(self, requested_dois, scored_documents, should_request):
        if requested_dois:
            found_dois = set([
                getattr(
                    scored_document.typed_document,
                    scored_document.typed_document.WhichOneof('document')
                ).doi
                for scored_document in scored_documents
            ])
            if len(found_dois) < len(requested_dois):
                if should_request:
                    for doi in requested_dois:
                        if doi not in found_dois:
                            await self.request_doi_delivery(doi=doi)
                raise NeedRetryError()

    def resolve_index_aliases(self, request_index_aliases, processed_query):
        """
        Derives requested indices through request and query
        """
        index_aliases = set([index_alias for index_alias in request_index_aliases])
        index_aliases_from_query = processed_query.context.index_aliases or index_aliases
        return tuple(sorted([index_alias for index_alias in index_aliases_from_query if index_alias in index_aliases]))

    def scorer(self, processed_query, index_alias):
        if processed_query.context.order_by:
            return search_service_pb2.Scorer(order_by=processed_query.context.order_by[0])

        if processed_query.is_empty():
            return None

        eval_scorer_builder = EvalScorerBuilder()
        if index_alias == 'scimag':
            eval_scorer_builder.add_exp_decay(
                field_name='issued_at',
                origin=(
                        processed_query.context.query_point_of_time
                        - processed_query.context.query_point_of_time % 86400
                ),
                scale=timedelta(days=365.25 * 14),
                offset=timedelta(days=30),
                decay=0.85,
            )
            eval_scorer_builder.add_fastsigm('page_rank + 1', 0.45)
        elif index_alias == 'scitech':
            eval_scorer_builder.ops.append('0.7235')
        return eval_scorer_builder.build()

    async def process_query(self, query, languages, context):
        try:
            return self.query_preprocessor.process(query, languages)
        except ParseError:
            return await context.abort(StatusCode.INVALID_ARGUMENT, 'parse_error')

    async def base_search(
        self,
        search_requests: List[SearchRequest],
        collector_descriptors: List[str],
        request_id: str,
        session_id: str,
        user_id: Optional[str] = None,
        skip_cache_loading: Optional[Union[bool, str]] = None,
        skip_cache_saving: Optional[Union[bool, str]] = None,
        original_query: Optional[str] = None,
        query_tags: Optional[List[str]] = None,
    ):
        start = default_timer()

        skip_cache_saving = to_bool(skip_cache_saving)
        skip_cache_loading = to_bool(skip_cache_loading)

        cache_key = tuple(search_request.cache_key() for search_request in search_requests)
        meta_search_response = self.query_cache.get(cache_key)
        cache_hit = bool(meta_search_response)

        if not cache_hit or skip_cache_loading:
            requests = []
            for search_request in search_requests:
                requests.append(
                    self.summa_client.search(
                        index_alias=search_request.index_alias,
                        query=search_request.query,
                        collectors=search_request.collectors,
                        request_id=request_id,
                        session_id=session_id,
                        ignore_not_found=True,
                    )
                )
            search_responses = await asyncio.gather(*requests)
            meta_search_response = self.merge_search_responses(search_responses, collector_descriptors)
            if not skip_cache_saving:
                self.query_cache[cache_key] = meta_search_response

        logging.getLogger('query').info({
            'action': 'request',
            'cache_hit': cache_hit,
            'duration': default_timer() - start,
            'mode': 'search',
            'query': original_query,
            'request_id': request_id,
            'session_id': session_id,
            'query_tags': query_tags,
            'user_id': user_id,
        })

        return meta_search_response

    @aiogrpc_request_wrapper(log=False)
    async def meta_search(self, request, context, metadata):
        processed_query = await self.process_query(
            query=request.query,
            languages=dict(request.languages),
            context=context,
        )
        index_aliases = self.resolve_index_aliases(
            request_index_aliases=request.index_aliases,
            processed_query=processed_query,
        )
        search_requests = [
            SearchRequest(
                index_alias=index_alias,
                query=self.query_transformers[index_alias].apply_tree_transformers(processed_query).to_summa_query(),
                collectors=request.collectors,
            ) for index_alias in index_aliases
        ]
        collector_descriptors = [collector.WhichOneof('collector') for collector in request.collectors]

        return await self.base_search(
            search_requests=search_requests,
            collector_descriptors=collector_descriptors,
            request_id=metadata['request-id'],
            session_id=metadata['session-id'],
            user_id=metadata.get('user-id'),
            skip_cache_loading=metadata.get('skip-cache-loading'),
            skip_cache_saving=metadata.get('skip-cache-saving'),
            original_query=request.query,
            query_tags=[tag for tag in request.query_tags],
        )

    @aiogrpc_request_wrapper(log=False)
    async def search(self, request, context, metadata):
        preprocessed_query = await self.process_query(query=request.query, languages=request.language, context=context)
        index_aliases = self.resolve_index_aliases(
            request_index_aliases=request.index_aliases,
            processed_query=preprocessed_query,
        )

        page_size = request.page_size or 5
        left_offset = request.page * page_size
        right_offset = left_offset + page_size

        search_requests = []
        for index_alias in index_aliases:
            processed_query = self.query_transformers[index_alias].apply_tree_transformers(preprocessed_query)
            search_requests.append(
                SearchRequest(
                    index_alias=index_alias,
                    query=processed_query.to_summa_query(),
                    collectors=[
                        search_service_pb2.Collector(
                            top_docs=search_service_pb2.TopDocsCollector(
                                limit=50,
                                scorer=self.scorer(processed_query, index_alias),
                                snippets=self.snippets[index_alias],
                                explain=processed_query.context.explain,
                            )
                        ),
                        search_service_pb2.Collector(count=search_service_pb2.CountCollector())
                    ],
                )
            )

        with suppress(RetryError):
            async for attempt in AsyncRetrying(
                retry=retry_if_exception_type(NeedRetryError),
                wait=wait_fixed(5),
                stop=stop_after_attempt(6)
            ):
                with attempt:
                    meta_search_response = await self.base_search(
                        search_requests=search_requests,
                        collector_descriptors=['top_docs', 'count'],
                        request_id=metadata['request-id'],
                        session_id=metadata['session-id'],
                        user_id=metadata.get('user-id'),
                        skip_cache_loading=attempt.retry_state.attempt_number > 1 or metadata.get('skip-cache-loading'),
                        skip_cache_saving=metadata.get('skip-cache-saving'),
                        original_query=request.query,
                        query_tags=[tag for tag in request.query_tags],
                    )
                    new_scored_documents = self.cast_top_docs_collector(
                        meta_search_response.collector_outputs[0].top_docs.scored_documents,
                    )
                    has_next = len(new_scored_documents) > right_offset
                    if 'scimag' in index_aliases:
                        await self.check_if_need_new_documents_by_dois(
                            requested_dois=processed_query.context.dois,
                            scored_documents=new_scored_documents,
                            should_request=attempt.retry_state.attempt_number == 1
                        )

        search_response_pb = meta_search_service_pb2.SearchResponse(
            scored_documents=new_scored_documents[left_offset:right_offset],
            has_next=has_next,
            count=meta_search_response.collector_outputs[1].count.count,
            query_language=processed_query.context.query_language,
        )

        return search_response_pb

    async def request_doi_delivery(self, doi):
        document_operation = operation_pb2.DocumentOperation(
            update_document=operation_pb2.UpdateDocument(
                should_fill_from_external_source=True,
                full_text_index=True,
                full_text_index_commit=True,
                typed_document=typed_document_pb2.TypedDocument(scimag=scimag_pb2.Scimag(doi=doi)),
            ),
        )
        self.operation_logger.info(MessageToDict(document_operation, preserving_proto_field_name=True))
