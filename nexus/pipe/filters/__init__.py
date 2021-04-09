from aiokit import AioThing
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb


class DocumentOperationFilter(AioThing):
    def __init__(self, operation, document=None):
        super().__init__()
        self.operation = operation
        self.document = document

    def filter(self, document_operation_pb: DocumentOperationPb) -> bool:
        if document_operation_pb.WhichOneof('operation') != self.operation:
            return False
        if self.document is not None:
            operation = getattr(document_operation_pb, document_operation_pb.WhichOneof('operation'))
            return operation.typed_document.HasField(self.document)
        return True
