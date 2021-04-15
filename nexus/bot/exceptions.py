import logging

from izihawa_utils.exceptions import BaseError


class BannedUserError(BaseError):
    level = logging.WARNING
    code = 'banned_user_error'

    def __init__(self, ban_timeout: int):
        self.ban_timeout = ban_timeout


class MessageHasBeenDeletedError(BaseError):
    level = logging.WARNING
    code = 'message_has_been_deleted_error'


class UnknownFileFormatError(BaseError):
    level = logging.WARNING
    code = 'unknown_file_format_error'


class UnknownSchemaError(BaseError):
    code = 'unknown_schema_error'
