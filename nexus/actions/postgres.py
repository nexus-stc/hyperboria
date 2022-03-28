import orjson as json
from izihawa_utils.common import filter_none
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from summa.proto.proto_grpc_py_pb import index_pb2 as index_pb

from .base import BaseAction


class ToThinScimagPbAction(BaseAction):
    async def do(self, item: dict) -> ScimagPb:
        return ScimagPb(doi=item['doi'])


class ScitechToIndexOperationBytesAction(BaseAction):
    restricted_column_set = [
        'extension',
        'fiction_id',
        'filesize',
        'has_duplicates',
        'ipfs_multihashes',
        'libgen_id',
        'md5',
        'original_id',
    ]

    async def do(self, item: dict) -> bytes:
        # if item['original_id'] is not None:
        #     item = {rc: item[rc] for rc in self.restricted_column_set}
        return index_pb.IndexOperation(
            index_document=index_pb.IndexDocumentOperation(
                document=json.dumps(filter_none(item)),
                reindex=True,
            ),
        ).SerializeToString()
