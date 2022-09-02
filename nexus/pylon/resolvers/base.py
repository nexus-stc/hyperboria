from typing import (
    AsyncIterable,
    Dict,
)

from nexus.pylon.network_agent import NetworkAgent
from nexus.pylon.prepared_request import PreparedRequest


class BaseResolver(NetworkAgent):
    def __str__(self):
        return self.__class__.__name__

    async def resolve(self, params: Dict) -> AsyncIterable[PreparedRequest]:
        raise NotImplementedError("`resolve` for BaseSource is not implemented")
