from html import unescape

from bs4 import BeautifulSoup
from nexus.actions.common import canonize_doi
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.operation_pb2 import UpdateDocument as UpdateDocumentPb
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from nexus.nlptools.language_detect import detect_language
from nexus.nlptools.utils import (
    despace,
    despace_full,
)

from .base import BaseAction


class CleanScitechAction(BaseAction):
    async def do(self, scitech_pb: ScitechPb) -> ScitechPb:
        if scitech_pb.authors:
            for i, author in enumerate(scitech_pb.authors):
                scitech_pb.authors[i] = despace_full(author)

        if scitech_pb.description:
            description_soup = BeautifulSoup(unescape(scitech_pb.description), 'lxml')
            for line in description_soup.select(r'p, title, jats\:title, jats\:p'):
                line.replace_with(f'\n{line.text.strip()}\n')
            scitech_pb.description = despace(description_soup.text.strip())

        scitech_pb.series = despace_full(scitech_pb.series)
        scitech_pb.title = despace_full(scitech_pb.title)

        if not scitech_pb.meta_language and (scitech_pb.title or scitech_pb.description):
            detected_language = detect_language(f'{scitech_pb.title} {scitech_pb.description }')
            if detected_language:
                scitech_pb.meta_language = detected_language
        if not scitech_pb.language:
            scitech_pb.language = scitech_pb.meta_language

        scitech_pb.md5 = scitech_pb.md5.lower()
        scitech_pb.extension = scitech_pb.extension.lower()
        scitech_pb.doi = canonize_doi(scitech_pb.doi)
        if scitech_pb.edition == 'None':
            scitech_pb.edition = ''
        return scitech_pb


class ScitechPbToDocumentOperationBytesAction(BaseAction):
    async def do(self, item: ScitechPb) -> bytes:
        document_operation_pb = DocumentOperationPb(
            update_document=UpdateDocumentPb(
                reindex=True,
                typed_document=TypedDocumentPb(scitech=item),
            ),
        )
        return document_operation_pb.SerializeToString()
