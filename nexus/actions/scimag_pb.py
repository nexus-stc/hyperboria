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
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb

from .base import BaseAction
from .common import canonize_doi


class DetectLanguageAction(BaseAction):
    async def do(self, scimag_pb: ScimagPb) -> ScimagPb:
        if scimag_pb.title or scimag_pb.abstract or scimag_pb.content:
            detected_language = detect_language(f'{scimag_pb.title} {scimag_pb.abstract} {scimag_pb.content}')
            if detected_language:
                scimag_pb.meta_language = detected_language
                if scimag_pb.content:
                    scimag_pb.language = detected_language
        if not scimag_pb.language:
            scimag_pb.language = scimag_pb.meta_language
        return scimag_pb


class CleanAction(BaseAction):
    async def do(self, scimag_pb: ScimagPb) -> ScimagPb:
        if scimag_pb.abstract:
            abstract_soup = BeautifulSoup(unescape(scimag_pb.abstract), 'lxml')
            for line in abstract_soup.select(r'p, title, jats\:title, jats\:p'):
                line.replace_with(f'\n{line.text.strip()}\n')
            scimag_pb.abstract = despace(abstract_soup.text.strip())
        if scimag_pb.title:
            scimag_pb.title = despace_full(BeautifulSoup(unescape(scimag_pb.title), 'lxml').text.strip())
        if scimag_pb.authors:
            for i, author in enumerate(scimag_pb.authors):
                scimag_pb.authors[i] = despace_full(BeautifulSoup(unescape(author), 'lxml').text.strip())
        if scimag_pb.container_title:
            scimag_pb.container_title = scimag_pb.container_title.replace(
                '<html_ent glyph="@lt;" ascii="&lt;"/>'
                'html_ent glyph="@amp;" ascii="<html_ent glyph="@amp;" ascii="&amp;"/>"/'
                '<html_ent glyph="@gt;" ascii="&gt;"/>',
                '&'
            )
            scimag_pb.container_title = scimag_pb.container_title.replace('<html_ent glyph="@amp;" ascii="&amp;"/>', '&')
            scimag_pb.container_title = scimag_pb.container_title.replace(
                '<html_ent glyph="@lt;" ascii="&lt;"/>'
                'html_ent glyph="@amp;" ascii="&amp;"/'
                '<html_ent glyph="@gt;" ascii="&gt;"/>',
                '&'
            )
            scimag_pb.container_title = scimag_pb.container_title.replace('<html_ent glyph="@lt;" ascii="&lt;"/>', '')
            scimag_pb.container_title = scimag_pb.container_title.replace('<html_ent glyph="@gt;" ascii="&gt;"/>', '')
            scimag_pb.container_title = BeautifulSoup(unescape(scimag_pb.container_title), 'lxml').text.strip()
        if scimag_pb.doi:
            scimag_pb.doi = canonize_doi(scimag_pb.doi)
        if scimag_pb.references:
            canonized_references = list(map(canonize_doi, scimag_pb.references))
            del scimag_pb.references[:]
            scimag_pb.references.extend(canonized_references)
        return scimag_pb


class ToDocumentOperationBytesAction(BaseAction):
    def __init__(self, full_text_index: bool, should_fill_from_external_source: bool):
        super().__init__()
        self.full_text_index = full_text_index
        self.should_fill_from_external_source = should_fill_from_external_source

    async def do(self, item: ScimagPb) -> bytes:
        document_operation_pb = DocumentOperationPb(
            update_document=UpdateDocumentPb(
                full_text_index=self.full_text_index,
                should_fill_from_external_source=self.should_fill_from_external_source,
                typed_document=TypedDocumentPb(scimag=item),
            ),
        )
        return document_operation_pb.SerializeToString()
