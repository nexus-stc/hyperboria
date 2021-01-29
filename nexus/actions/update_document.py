from aiosumma import SummaHttpClient
from nexus.cognitron.schema import coders
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb

from .base import BaseAction


class SendDocumentOperationUpdateDocumentPbToSummaAction(BaseAction):
    def __init__(self, summa):
        super().__init__()
        self.summa_client = SummaHttpClient(**summa)
        self.waits.append(self.summa_client)

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        schema = update_document_pb.typed_document.WhichOneof('document')
        document = getattr(update_document_pb.typed_document, schema)
        original_id = getattr(document, 'original_id', None)
        if not update_document_pb.reindex or original_id:
            return document_operation_pb
        document_tantivy = coders[schema].encode_document(document)
        await self.summa_client.put_document(schema, document_tantivy)
        if update_document_pb.commit:
            await self.summa_client.commit(schema)
        return document_operation_pb
