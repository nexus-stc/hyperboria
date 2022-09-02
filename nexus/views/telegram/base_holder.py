from urllib.parse import quote

import orjson as json
from izihawa_nlptools.utils import (
    cast_string_to_single_string,
    escape_format,
)
from izihawa_types.safecast import safe_int
from nexus.models.proto import (
    scimag_pb2,
    scitech_pb2,
    typed_document_pb2,
)

from .common import (
    TooLongQueryError,
    encode_query_to_deep_link,
)
from .scimag import (
    ScimagButtonsBuilder,
    ScimagViewBuilder,
)
from .scitech import (
    ScitechButtonsBuilder,
    ScitechViewBuilder,
)


class BaseHolder:
    multihash_ix = 0

    views_registry = {
        'scimag': ScimagViewBuilder,
        'scitech': ScitechViewBuilder,
    }

    def __init__(self, document_pb, snippets=None):
        self.document_pb = document_pb
        self.snippets = snippets

    def __getattr__(self, name):
        return getattr(self.document_pb, name)

    @classmethod
    def create(cls, typed_document_pb, snippets=None):
        match typed_document_pb.WhichOneof('document'):
            case 'scimag':
                return ScimagHolder(typed_document_pb.scimag, snippets)
            case 'scitech':
                return ScitechHolder(typed_document_pb.scitech, snippets)
            case _:
                raise ValueError('Unknown type')

    @classmethod
    def create_from_document(cls, document):
        match document.index_alias:
            case 'scimag':
                return ScimagHolder(scimag_pb2.Scimag(**json.loads(document.document)), getattr(document, 'snippets', None))
            case 'scitech':
                return ScitechHolder(scitech_pb2.Scitech(**json.loads(document.document)), getattr(document, 'snippets', None))
            case _:
                raise ValueError('Unknown index alias')

    def get_filename(self) -> str:
        limit = 55
        filename = cast_string_to_single_string(
            self.view_builder().add_authors(et_al=False).add_title(bold=False).add_formatted_datetime().build().lower()
        )

        chars = []
        size = 0
        hit_limit = False

        for c in filename:
            current_size = size + len(c.encode())
            if current_size > limit:
                hit_limit = True
                break
            chars.append(c)
            size = current_size

        filename = ''.join(chars)
        if hit_limit:
            glyph = filename.rfind('-')
            if glyph != -1:
                filename = filename[:glyph]

        if not filename:
            if self.doi:
                filename = quote(self.doi, safe='')
            else:
                filename = self.md5

        return f'{filename}.{self.get_extension()}'

    def get_extension(self) -> str:
        return 'pdf'

    def get_formatted_filesize(self) -> str:
        if self.filesize:
            filesize = max(1024, self.filesize)
            return '{:.1f}Mb'.format(float(filesize) / (1024 * 1024))
        else:
            return ''

    def get_formatted_filedata(self, show_format=True, show_language=True, show_filesize=False) -> str:
        parts = []
        if show_language:
            if self.meta_language and self.meta_language != 'en':
                parts.append(self.meta_language.upper())
            elif self.language and self.language != 'en':
                parts.append(self.language.upper())
        if show_format:
            extension = self.get_extension().upper()
            if extension != 'PDF':
                parts.append(extension)
        if self.filesize and show_filesize:
            parts.append(self.get_formatted_filesize())
        return ' | '.join(parts)

    def get_ipfs_gateway_link(self):
        ipfs_link = (
            f'https://ipfs.io/ipfs/{self.ipfs_multihashes[self.multihash_ix]}?'
            f'filename={quote(self.get_filename())}'
        )
        return f'[IPFS.io]({ipfs_link})'

    def get_ipfs_link(self):
        ipfs_link = (
            f'ipfs://{self.ipfs_multihashes[self.multihash_ix]}?'
            f'filename={quote(self.get_filename())}'
        )
        return f'[IPFS]({ipfs_link})'

    def get_doi_link(self):
        return f'[{self.doi}](https://doi.org/{quote(self.doi)})'

    def encode_link(self, bot_name, text, query):
        try:
            encoded_query = encode_query_to_deep_link(query, bot_name)
            if text:
                return f'[{text}]({encoded_query})'
            else:
                return encoded_query
        except TooLongQueryError:
            return text

    def get_deep_id_link(self, bot_name, text=None):
        query = f'id:{self.id}'
        return self.encode_link(bot_name, text, query)

    def get_deep_author_link(self, bot_name, author):
        query = f'authors:"{author}"'
        return self.encode_link(bot_name, author, query)

    def get_deep_tag_link(self, bot_name, tag):
        query = f'tags:"{tag}"'
        return self.encode_link(bot_name, tag, query)

    def generate_links(self, bot_name, bot_link_text='Nexus Bot'):
        links = [
            self.get_deep_id_link(bot_name=bot_name, text=bot_link_text)
        ]
        if self.ipfs_multihashes:
            links.append(self.get_ipfs_gateway_link())
        if self.doi:
            links.append(self.get_doi_link())
        return links

    def generate_tags_links(self, bot_name):
        if self.tags:
            links = [self.get_deep_tag_link(bot_name=bot_name, tag=escape_format(tag)) for tag in self.tags]
            return links
        return []

    def has_field(self, name):
        try:
            return self.document_pb.HasField(name)
        except ValueError:
            return hasattr(self.document_pb, name)

    def get_typed_document(self):
        return typed_document_pb2.TypedDocument(**{self.index_alias: self.document_pb})


class ScimagHolder(BaseHolder):
    index_alias = 'scimag'

    def view_builder(self, user_language=None):
        return ScimagViewBuilder(document_holder=self, user_language=user_language)

    def buttons_builder(self, user_language):
        return ScimagButtonsBuilder(document_holder=self, user_language=user_language)

    def get_download_command(self, session_id: str, position: int = 0) -> str:
        return f'/dla_{session_id}_{self.id}_{position}'

    def get_view_command(self, session_id: str, message_id: int, position: int = 0) -> str:
        return f'/va_{session_id}_{message_id}_{self.id}_{position}'

    def get_cover_url(self):
        return None

    def get_thumb_url(self):
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Science-symbol-2.svg/2048px-Science-symbol-2.svg.png'


class ScitechHolder(BaseHolder):
    index_alias = 'scitech'

    def view_builder(self, user_language=None):
        return ScitechViewBuilder(document_holder=self, user_language=user_language)

    def buttons_builder(self, user_language):
        return ScitechButtonsBuilder(document_holder=self, user_language=user_language)

    def get_download_command(self, session_id: str, position: int = 0) -> str:
        return f'/dlb_{session_id}_{self.id}_{position}'

    def get_view_command(self, session_id: str, message_id: int, position: int = 0) -> str:
        return f'/vb_{session_id}_{message_id}_{self.id}_{position}'

    def get_cover_url(self):
        if self.cu:
            local_parts = self.cu.split('/')
            if len(local_parts) == 2 and safe_int(local_parts[0]) is not None:
                return f'http://gen.lib.rus.ec/covers/{self.cu}'
            if len(local_parts) == 1:
                bulk_id = (self.libgen_id - (self.libgen_id % 1000))
                return f'http://gen.lib.rus.ec/covers/{bulk_id}/{self.cu}'
            return self.cu
        if self.libgen_id or self.fiction_id:
            if self.libgen_id:
                bulk_id = (self.libgen_id - (self.libgen_id % 1000))
                r = f'covers/{bulk_id}/{self.md5}'
            elif self.fiction_id:
                bulk_id = (self.fiction_id - (self.fiction_id % 1000))
                r = f'fictioncovers/{bulk_id}/{self.md5}'
            else:
                return None
            if self.cu_suf:
                r += f'-{self.cu_suf}'
            return f'http://gen.lib.rus.ec/{r}.jpg'

    def get_thumb_url(self):
        return self.get_cover_url()

    def get_extension(self):
        return self.document_pb.extension
