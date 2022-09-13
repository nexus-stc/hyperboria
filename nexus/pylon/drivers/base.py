from typing import (
    Dict,
    List,
    Optional,
)

from izihawa_utils.importlib import import_object
from nexus.pylon.network_agent import NetworkAgent
from nexus.pylon.prepared_request import PreparedRequest
from nexus.pylon.proxy_manager import ProxyManager


class BaseDriver(NetworkAgent):
    def __init__(
        self,
        config,
        validator=None,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        super().__init__(proxy_list=proxy_list, proxy_manager=proxy_manager)
        self.config = config

        validator_cls = 'nexus.pylon.validators.PdfValidator'
        if validator and 'class' in validator:
            validator_cls = validator['class']
        validator_cls = import_object(validator_cls)

        self.validator = validator_cls

    def __str__(self):
        return self.__class__.__name__

    async def execute_prepared_file_request(
        self,
        prepared_file_request: PreparedRequest,
        params: Dict,
    ):
        raise NotImplementedError()
