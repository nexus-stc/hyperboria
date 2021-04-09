from typing import (
    List,
    Optional,
    Tuple,
    Union,
)

from aiokit import AioThing
from grpc import StatusCode
from grpc.experimental.aio import (
    AioRpcError,
    insecure_channel,
)
from lru import LRU
from nexus.meta_api.proto.documents_service_pb2 import \
    RollRequest as RollRequestPb
from nexus.meta_api.proto.documents_service_pb2 import \
    RollResponse as RollResponsePb
from nexus.meta_api.proto.documents_service_pb2 import \
    TypedDocumentRequest as TypedDocumentRequestPb
from nexus.meta_api.proto.documents_service_pb2_grpc import DocumentsStub
from nexus.meta_api.proto.meta_search_service_pb2 import \
    SearchRequest as SearchRequestPb
from nexus.meta_api.proto.meta_search_service_pb2 import \
    SearchResponse as SearchResponsePb
from nexus.meta_api.proto.meta_search_service_pb2_grpc import MetaSearchStub
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_fixed,
)


class MetaApiGrpcClient(AioThing):
    def __init__(self, base_url):
        super().__init__()
        self.channel = insecure_channel(base_url, [
            ('grpc.dns_min_time_between_resolutions_ms', 1000),
            ('grpc.initial_reconnect_backoff_ms', 1000),
            ('grpc.lb_policy_name', 'round_robin'),
            ('grpc.min_reconnect_backoff_ms', 1000),
            ('grpc.max_reconnect_backoff_ms', 2000),
        ])
        self.meta_search_stub = MetaSearchStub(self.channel)
        self.documents_stub = DocumentsStub(self.channel)
        self.cache = LRU(4096)

    async def start(self):
        await self.channel.channel_ready()

    async def stop(self):
        await self.channel.close()

    async def get(
        self,
        schema: str,
        document_id: int,
        position: Optional[int] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> TypedDocumentPb:
        return await self.documents_stub.get(
            TypedDocumentRequestPb(
                schema=schema,
                document_id=document_id,
                position=position,
                session_id=session_id,
                user_id=user_id,
            ),
            metadata=(
                ('request-id', request_id),
            ),
        )

    async def roll(
        self,
        language: Optional[str] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> RollResponsePb:
        return await self.documents_stub.roll(
            RollRequestPb(
                language=language,
                session_id=session_id,
                user_id=user_id,
            ),
            metadata=(
                ('request-id', request_id),
            ),
        )

    @retry(
        retry=retry_if_exception(
            lambda e: isinstance(e, AioRpcError) and (
                e.code() == StatusCode.CANCELLED
                or e.code() == StatusCode.UNAVAILABLE
            )
        ),
        reraise=True,
        stop=stop_after_attempt(5),
        wait=wait_fixed(2),
    )
    async def search(
        self,
        schemas: Union[List[str], Tuple[str]],
        query: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        language: Optional[str] = None,
        request_id: Optional[str] = None,
        session_id: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> SearchResponsePb:
        return await self.meta_search_stub.search(
            SearchRequestPb(
                schemas=schemas,
                query=query,
                page=page,
                page_size=page_size,
                language=language,
                session_id=session_id,
                user_id=user_id,
            ),
            metadata=(
                ('request-id', request_id),
            ),
        )
