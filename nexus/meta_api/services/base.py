import logging

import orjson as json
from library.aiogrpctools.base import BaseService as LibraryBaseService
from nexus.meta_api.proto import \
    search_service_pb2 as nexus_meta_api_search_service_pb
from nexus.models.proto import (
    scimag_pb2,
    scitech_pb2,
    typed_document_pb2,
)
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb


class BaseService(LibraryBaseService):
    pb_registry = {
        'scimag': ScimagPb,
        'scitech': ScitechPb,
    }

    def __init__(self, application, stat_provider, summa_client):
        super().__init__(application=application, service_name='meta_api')
        self.stat_provider = stat_provider
        self.summa_client = summa_client
        self.operation_logger = logging.getLogger('operation')

    def cast_top_docs_collector(self, scored_documents):
        new_scored_documents = []
        for scored_document in scored_documents:
            document = json.loads(scored_document.document)
            new_scored_documents.append(nexus_meta_api_search_service_pb.ScoredDocument(
                typed_document=typed_document_pb2.TypedDocument(
                    **{scored_document.index_alias: self.pb_registry[scored_document.index_alias](**document)},
                ),
                position=scored_document.position,
                score=float(getattr(scored_document.score, scored_document.score.WhichOneof('score'))),
                snippets=scored_document.snippets,
            ))
        return new_scored_documents

    def cast_reservoir_sampling_collector(self, index_alias, documents):
        new_scored_documents = []
        for position, document in enumerate(documents):
            document = json.loads(document)
            new_scored_documents.append(nexus_meta_api_search_service_pb.ScoredDocument(
                typed_document=TypedDocumentPb(
                    **{index_alias: self.pb_registry[index_alias](**document)},
                ),
                position=position,
                score=1.0,
            ))
        return new_scored_documents
