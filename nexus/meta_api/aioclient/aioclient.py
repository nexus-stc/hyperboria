from typing import (
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

from aiogrpcclient import (
    BaseGrpcClient,
    expose,
)
from izihawa_utils.pb_to_json import ParseDict
from nexus.meta_api.proto import (
    documents_service_pb2,
    documents_service_pb2_grpc,
    search_service_pb2,
    search_service_pb2_grpc,
)
from nexus.models.proto import typed_document_pb2


class MetaApiGrpcClient(BaseGrpcClient):
    stub_clses = {
        'documents': documents_service_pb2_grpc.DocumentsStub,
        'search': search_service_pb2_grpc.SearchStub,
    }

    @expose
    async def get(
        self,
        index_alias: str,
        document_id: int,
        mode: str,
        user_id: str,
        position: Optional[int] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> typed_document_pb2.TypedDocument:
        return await self.stubs['documents'].get(
            documents_service_pb2.TypedDocumentRequest(
                index_alias=index_alias,
                document_id=document_id,
                mode=mode,
                position=position,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
            ),
        )

    @expose(with_from_file=True)
    async def search(
        self,
        index_aliases: Union[List[str], Tuple[str]],
        query: str,
        user_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        language: Optional[str] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> search_service_pb2.SearchResponse:
        return await self.stubs['search'].search(
            search_service_pb2.SearchRequest(
                index_aliases=index_aliases,
                query=query,
                page=page,
                page_size=page_size,
                language=language,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
            ),
        )

    @expose(with_from_file=True)
    async def search(
        self,
        index_aliases: Union[List[str], Tuple[str]],
        query: str,
        user_id: str,
        query_tags: Optional[List] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        language: Optional[str] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> search_service_pb2.SearchResponse:
        return await self.stubs['search'].search(
            search_service_pb2.SearchRequest(
                index_aliases=index_aliases,
                query=query,
                query_tags=query_tags,
                page=page,
                page_size=page_size,
                language=language,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
            ),
        )

    @expose(with_from_file=True)
    async def meta_search(
        self,
        index_aliases: Union[List[str], Tuple[str]],
        query: str,
        collectors: List,
        languages: Optional[Dict[str, float]] = None,
        query_tags: Optional[List] = None,
        user_id: Optional[str] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        skip_cache_loading: Optional[bool] = False,
        skip_cache_saving: Optional[bool] = False,
    ) -> search_service_pb2.MetaSearchResponse:
        return await self.stubs['search'].meta_search(
            ParseDict({
                'index_aliases': index_aliases,
                'query': query,
                'languages': languages,
                'collectors': collectors,
                'query_tags': query_tags,
            }, search_service_pb2.MetaSearchRequest()),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
                ('skip-cache-loading', str(int(skip_cache_loading))),
                ('skip-cache-saving', str(int(skip_cache_saving))),
            ),
        )
