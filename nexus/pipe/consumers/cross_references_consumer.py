from nexus.models.proto.operation_pb2 import \
    CrossReferenceOperation as CrossReferenceOperationPb

from .base import (
    BaseBulkConsumer,
    BasePbConsumer,
)


class CrossReferencesConsumer(BasePbConsumer):
    pb_class = CrossReferenceOperationPb


class CrossReferencesBulkConsumer(BaseBulkConsumer, CrossReferencesConsumer):
    pass
