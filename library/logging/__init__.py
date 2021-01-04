import logging
import logging.config
import sys

from izihawa_utils.exceptions import BaseError
from izihawa_utils.file import mkdir_p
from library.logging.formatters import (
    DefaultFormatter,
    DefaultHttpFormatter,
)
from library.logging.handlers import QueueHandler
from prometheus_client import Counter

error_counter = Counter('errors_total', 'counter for error.log')


def configure_logging(config, make_path=True):
    if config.get('application', {}).get('debug', False) or 'logging' not in config:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        if make_path:
            mkdir_p(config['log_path'])
        logging.config.dictConfig(config['logging'])


def error_log(e, level=logging.ERROR, **fields):
    level = getattr(e, 'level', level)
    if level == logging.ERROR:
        error_counter.inc()
    if isinstance(e, BaseError):
        e = e.as_internal_dict()
        e.update(fields)
    elif fields:
        e = {'error': str(e), **fields}
    logging.getLogger('error').log(
        msg=e,
        level=level
    )


__all__ = [
    'DefaultFormatter', 'DefaultHttpFormatter',
    'QueueHandler', 'configure_logging', 'error_log',
]
