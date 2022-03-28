from .crossref_api import CrossrefApiJob
from .libgen_api import LibgenApiJob
from .postgres import PostgresJob
from .self_feed import SelfFeedJob

__all__ = ['CrossrefApiJob', 'LibgenApiJob', 'PostgresJob', 'SelfFeedJob']
