from typing import Union

from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb

from .scimag import ScimagView
from .scitech import ScitechView

pb_registry = {
    'scimag': ScimagPb,
    'scitech': ScitechPb,
}

views_registry = {
    'scimag': ScimagView,
    'scitech': ScitechView,
}


def parse_typed_document_to_view(typed_document_pb) -> Union[ScimagView, ScitechView]:
    document_pb = getattr(typed_document_pb, typed_document_pb.WhichOneof('document'))
    return views_registry[typed_document_pb.WhichOneof('document')](document_pb)
