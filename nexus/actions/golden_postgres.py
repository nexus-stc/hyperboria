from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb

from .base import BaseAction


class GoldenPostgresToThinScimagPbAction(BaseAction):
    async def do(self, item: dict) -> ScimagPb:
        return ScimagPb(doi=item['doi'])
