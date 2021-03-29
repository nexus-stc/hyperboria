from aiosumma import SummaHttpClient
from izihawa_utils.pb_to_json import MessageToDict
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
        casted_document = MessageToDict(document, preserving_proto_field_name=True)
        # ToDo: Required to rework checking for extra fields in document
        # ToDo: It is needed to go to actual schema and load real fields and then check against them
        casted_document.pop('is_deleted', None)
        casted_document.pop('meta_language', None)
        casted_document.pop('type', None)
        await self.summa_client.put_document(schema, casted_document)
        if update_document_pb.commit:
            await self.summa_client.commit(schema)
        return document_operation_pb
