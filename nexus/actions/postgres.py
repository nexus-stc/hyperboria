import orjson as json
from izihawa_utils.common import filter_none
from summa.proto import index_service_pb2 as index_service_pb

from .base import BaseAction


class ScimagToIndexOperationBytesAction(BaseAction):
    async def do(self, item: dict) -> bytes:
        return index_service_pb.IndexOperation(
            index_document=index_service_pb.IndexDocumentOperation(
                document=json.dumps(filter_none(item)),
            ),
        ).SerializeToString()


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
        return index_service_pb.IndexOperation(
            index_document=index_service_pb.IndexDocumentOperation(
                document=json.dumps(filter_none(item)),
            ),
        ).SerializeToString()
