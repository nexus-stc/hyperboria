from html import unescape

from bs4 import BeautifulSoup
from izihawa_nlptools.language_detect import detect_language
from izihawa_nlptools.utils import (
    despace,
    despace_full,
)
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.operation_pb2 import UpdateDocument as UpdateDocumentPb
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb

from .base import BaseAction
from .common import canonize_doi

editions = {
    '1st': '1',
    '1st ed.': '1',
    'first edition': '1',
    'none': '',
    '2nd': '2',
    'paperback': '',
    'hardcover': '',
    '1st ed': '1',
    'reprint': '',
    '2nd ed': '2',
    '1. aufl.': '1',
    '0': '',
    'illustrated edition': '',
    '3rd': '3',
    '1ª': '1',
    '1st edition': '1',
    'kindle edition': '',
    '1st edition.': '1',
    '1st ed. 2019': '1',
    '3rd ed': '3',
    'second edition': '2',
    '2-е': '2',
    'original': '',
    '4th': '4',
    '1st ed. 2020': '1',
    'annotated edition': '',
    '2nd edition': '2',
    '2nd ed.': '2',
    '5th': '5',
    '1. aufl': '1',
    '4th ed': '4',
    'ebook': '',
    '1. auflage': '1',
    'first edition.': '1',
    '3rd edition': '3',
    '10th ed': '10',
    '2-е издание, переработанное и дополненное': '2',
}


class CleanAction(BaseAction):
    async def do(self, scitech_pb: ScitechPb) -> ScitechPb:
        if scitech_pb.authors:
            for i, author in enumerate(scitech_pb.authors):
                scitech_pb.authors[i] = despace_full(author)

        if scitech_pb.description:
            description_soup = BeautifulSoup(unescape(scitech_pb.description), 'lxml')
            for line in description_soup.select(r'p, title, jats\:title, jats\:p'):
                line.replace_with(f'\n{line.text.strip()}\n')
            scitech_pb.description = despace(description_soup.text.strip())

        scitech_pb.periodical = despace_full(scitech_pb.periodical)
        scitech_pb.volume = despace_full(scitech_pb.volume)
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
        if scitech_pb.edition is not None:
            edition = scitech_pb.edition.lower()
            scitech_pb.edition = editions.get(edition, edition)
        return scitech_pb


class ToDocumentOperationBytesAction(BaseAction):
    def __init__(self, full_text_index: bool):
        super().__init__()
        self.full_text_index = full_text_index

    async def do(self, item: ScitechPb) -> bytes:
        document_operation_pb = DocumentOperationPb(
            update_document=UpdateDocumentPb(
                full_text_index=self.full_text_index,
                typed_document=TypedDocumentPb(scitech=item),
            ),
        )
        return document_operation_pb.SerializeToString()
