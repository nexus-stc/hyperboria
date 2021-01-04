from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb

from .base import (
    BaseBulkConsumer,
    BaseJsonConsumer,
    BasePbConsumer,
)


class DocumentOperationsConsumer(BasePbConsumer):
    pb_class = DocumentOperationPb


class DocumentOperationsJsonConsumer(BaseJsonConsumer):
    pb_class = DocumentOperationPb


class DocumentOperationsBulkConsumer(BaseBulkConsumer, DocumentOperationsConsumer):
    pass
