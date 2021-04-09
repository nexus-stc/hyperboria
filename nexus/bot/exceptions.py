from izihawa_utils.exceptions import BaseError


class UnknownFileFormatError(BaseError):
    code = 'unknown_file_format_error'


class UnknownSchemaError(BaseError):
    code = 'unknown_schema_error'
