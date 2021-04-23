from aiosumma.exceptions import (
    InvalidSyntaxError,
    QueryTimeoutError,
)
from grpc import StatusCode
from library.aiogrpctools.base import BaseService as LibraryBaseService
from nexus.meta_api.query_extensionner.grammar.parser import ParseError


class BaseService(LibraryBaseService):
    error_mapping = {
        InvalidSyntaxError: (StatusCode.INVALID_ARGUMENT, 'invalid_query_error'),
        ParseError: (StatusCode.INVALID_ARGUMENT, 'invalid_query_error'),
        QueryTimeoutError: (StatusCode.CANCELLED, 'cancelled_error'),
    }
