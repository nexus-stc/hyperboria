from izihawa_utils.exceptions import BaseError


class FileTooBigError(BaseError):
    code = 'file_too_big_error'


class UnavailableMetadataError(BaseError):
    code = 'unavailable_metadata_error'


class UnparsableDoiError(BaseError):
    code = 'unparsable_doi_error'
