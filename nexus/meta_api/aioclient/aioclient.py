from typing import (
    List,
    Optional,
    Tuple,
    Union,
)

from aiogrpcclient import BaseGrpcClient
from nexus.meta_api.proto.documents_service_pb2 import \
    RollRequest as RollRequestPb
from nexus.meta_api.proto.documents_service_pb2 import \
    RollResponse as RollResponsePb
from nexus.meta_api.proto.documents_service_pb2 import \
    TopMissedRequest as TopMissedRequestPb
from nexus.meta_api.proto.documents_service_pb2 import \
    TopMissedResponse as TopMissedResponsePb
from nexus.meta_api.proto.documents_service_pb2 import \
    TypedDocumentRequest as TypedDocumentRequestPb
from nexus.meta_api.proto.documents_service_pb2_grpc import DocumentsStub
from nexus.meta_api.proto.search_service_pb2 import \
    SearchRequest as SearchRequestPb
from nexus.meta_api.proto.search_service_pb2 import \
    SearchResponse as SearchResponsePb
from nexus.meta_api.proto.search_service_pb2_grpc import SearchStub
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb


class MetaApiGrpcClient(BaseGrpcClient):
    stub_clses = {
        'documents': DocumentsStub,
        'search': SearchStub,
    }

    async def get(
        self,
        index_alias: str,
        document_id: int,
        user_id: str,
        position: Optional[int] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> TypedDocumentPb:
        return await self.stubs['documents'].get(
            TypedDocumentRequestPb(
                index_alias=index_alias,
                document_id=document_id,
                position=position,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
            ),
        )

    async def roll(
        self,
        user_id: str,
        language: Optional[str] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> RollResponsePb:
        return await self.stubs['documents'].roll(
            RollRequestPb(
                language=language,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
            ),
        )

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
    ) -> SearchResponsePb:
        return await self.stubs['search'].search(
            SearchRequestPb(
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

    async def top_missed(
        self,
        page: int,
        page_size: int,
        user_id: str,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> TopMissedResponsePb:
        return await self.stubs['documents'].top_missed(
            TopMissedRequestPb(
                page=page,
                page_size=page_size,
            ),
            metadata=(
                ('request-id', request_id),
                ('session-id', session_id),
                ('user-id', user_id),
            ),
        )
