import datetime
from typing import Optional
from urllib.parse import quote

import numpy as np
from nexus.nlptools.utils import escape_format

from .common import encode_query_to_deep_link


class CustomDatetime:
    def __init__(self, dt: np.datetime64):
        self.dt = dt

    @property
    def year(self) -> int:
        return self.dt.astype('datetime64[Y]').astype(int) + 1970

    @property
    def month(self) -> int:
        return self.dt.astype('datetime64[M]').astype(int) % 12 + 1

    @property
    def day(self) -> int:
        return self.dt - self.dt.astype('datetime64[M]') + 1


class DoiMixin:
    def get_doi_link(self) -> str:
        if not self.doi:
            return ''
        escaped_doi = escape_format(self.doi)
        return f'[{escaped_doi}](https://doi.org/{quote(escaped_doi)})'


class AuthorMixin:
    def get_first_authors(self, et_al=True, first_n_authors=1) -> str:
        et_al_suffix = (' et al' if et_al else '')
        if self.authors:
            if len(self.authors) > first_n_authors:
                return '; '.join(self.authors[:first_n_authors]) + et_al_suffix
            elif len(self.authors) == 1:
                if self.authors[0].count(';') >= 1:
                    comma_authors = list(map(str.strip, self.authors[0].split(';')))
                    if len(comma_authors) > first_n_authors:
                        return '; '.join(comma_authors[:first_n_authors]) + et_al_suffix
                    else:
                        return '; '.join(comma_authors)
                return self.authors[0]
            else:
                return '; '.join(self.authors)
        return ''


class IssuedAtMixin:
    def get_issued_datetime(self) -> Optional[CustomDatetime]:
        if not self.has_field('issued_at'):
            return None
        return CustomDatetime(dt=np.datetime64(self.issued_at, 's'))

    def get_formatted_datetime(self) -> str:
        if self.has_field('issued_at'):
            dt = self.get_issued_datetime()
            try:
                ct = datetime.date(dt.year, dt.month, 1)
                if datetime.date.today() - datetime.timedelta(days=365) < ct:
                    return f'{dt.year}.{dt.month:02d}'
            except ValueError:
                pass
            return str(dt.year)


class FileMixin:
    def get_extension(self) -> str:
        return 'pdf'

    def get_formatted_filedata(self, show_format=True, show_language=True, show_filesize=False) -> str:
        parts = []
        if self.language and show_language:
            parts.append(self.language.upper())
        if show_format:
            parts.append(self.get_extension().upper())
        if self.filesize and show_filesize:
            parts.append(self.get_formatted_filesize())
        return ' | '.join(parts)

    def get_formatted_filesize(self) -> str:
        if self.filesize:
            filesize = max(1024, self.filesize)
            return '{:.1f}Mb'.format(float(filesize) / (1024 * 1024))
        else:
            return ''


class BaseView:
    schema = None
    multihash_ix = 0

    def __getattr__(self, name):
        return getattr(self.document_pb, name)

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

    def get_deep_link(self, bot_external_name, text=None):
        if not text:
            text = str(self.id)
        encoded_query = encode_query_to_deep_link(f'NID: {self.id}', bot_external_name)
        return f'[{text}]({encoded_query})'

    def generate_links(self, bot_external_name):
        links = [
            self.get_deep_link(bot_external_name=bot_external_name, text='Nexus Bot')
        ]
        if self.ipfs_multihashes:
            links.append(self.get_ipfs_gateway_link())
        if self.doi:
            links.append(self.get_doi_link())
        return links

    def has_field(self, name):
        return self.document_pb.HasField(name)
