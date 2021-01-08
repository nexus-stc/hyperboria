import logging

from izihawa_utils.exceptions import BaseError


class DownloadError(BaseError):
    level = logging.WARNING
    code = 'download_error'


class IncorrectMD5Error(DownloadError):
    code = 'incorrect_md5_error'


class UnresolvableSourceError(DownloadError):
    level = logging.WARNING
    code = 'unresolvable_source_error'


class UnavailableSourcesError(DownloadError):
    code = 'no_available_sources_error'


class NotFoundError(DownloadError):
    level = logging.WARNING
    code = 'not_found_error'


class RegexNotFoundError(DownloadError):
    level = logging.WARNING
    code = 'regex_not_found_error'


class BadResponseError(DownloadError):
    code = 'bad_response_error'


class InvalidDocumentForDownload(DownloadError):
    code = 'invalid_document_for_download'
