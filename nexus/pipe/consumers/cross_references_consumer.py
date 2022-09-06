from nexus.models.proto.operation_pb2 import \
    CrossReferenceOperation as CrossReferenceOperationPb

from .base import BasePbConsumer


class CrossReferencesConsumer(BasePbConsumer):
    pb_class = CrossReferenceOperationPb
