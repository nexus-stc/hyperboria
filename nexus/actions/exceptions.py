from typing import List

from izihawa_utils.exceptions import BaseError


class InterruptProcessing(BaseError):
    code = 'interrupt_processing'

    def __init__(self, doc_id, reason):
        super().__init__(doc_id=doc_id, reason=reason)


class ConflictError(BaseError):
    code = 'conflict_error'

    def __init__(self, document, duplicates: List[dict]):
        super().__init__(document=document, duplicates=duplicates)
