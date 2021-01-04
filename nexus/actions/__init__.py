from .update_document import SendDocumentOperationUpdateDocumentPbToSummaAction
from .update_document_scimag import (
    CleanDocumentOperationUpdateDocumentScimagPbAction,
    FillDocumentOperationUpdateDocumentScimagPbFromExternalSourceAction,
    SendDocumentOperationUpdateDocumentScimagPbReferencesToKafkaAction,
    SendDocumentOperationUpdateDocumentScimagPbToGoldenPostgresAction,
)
from .update_document_scitech import (
    CleanDocumentOperationUpdateDocumentScitechPbAction,
    SendDocumentOperationUpdateDocumentScitechPbToGoldenPostgresAction,
)

__all__ = [
    'CleanDocumentOperationUpdateDocumentScimagPbAction',
    'CleanDocumentOperationUpdateDocumentScitechPbAction',
    'FillDocumentOperationUpdateDocumentScimagPbFromExternalSourceAction',
    'SendDocumentOperationUpdateDocumentPbToSummaAction',
    'SendDocumentOperationUpdateDocumentScimagPbReferencesToKafkaAction',
    'SendDocumentOperationUpdateDocumentScimagPbToGoldenPostgresAction',
    'SendDocumentOperationUpdateDocumentScitechPbToGoldenPostgresAction',
]
