import math
from typing import (
    List,
    Optional,
    Tuple,
)
from urllib.parse import quote

from izihawa_utils.common import filter_none
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.nlptools.utils import (
    cast_string_to_single_string,
    escape_format,
)
from nexus.translations import t
from nexus.views.telegram.common import close_button
from telethon import Button

from .base import (
    AuthorMixin,
    BaseView,
    DoiMixin,
    FileMixin,
    IssuedAtMixin,
)

preprints = {'10.1101', '10.21203'}


class ScimagView(BaseView, AuthorMixin, DoiMixin, FileMixin, IssuedAtMixin):
    icon = '🔬'
    schema = 'scimag'
    multihash_ix = 1

    def __init__(self, document_pb: ScimagPb):
        self.document_pb = document_pb

    def generate_body(self, language: str, with_referenced_by: bool = False, limit: Optional[int] = None) -> str:
        head = self.icon
        title = self.get_robust_title()
        if title:
            head += f' **{title}**'

        doi = f'**DOI:** {self.get_doi_link()}'

        referenced_by = None
        if with_referenced_by:
            referenced_by = self.get_referenced_by(language=language)

        caption = '\n'.join(filter_none([head, doi, referenced_by, self.get_formatted_locator()]))

        if limit and len(caption) > limit:
            caption = '\n'.join(filter_none([head, doi, referenced_by]))
            if len(caption) > limit:
                subtract = len(self.icon + doi) + 1
                shorten_title = title[:(limit - subtract)]
                shorten_head = f'{self.icon} **{shorten_title}**'
                caption = '\n'.join(filter_none([shorten_head, doi, referenced_by]))
        return caption

    def get_download_command(self, session_id: str, position: int = 0) -> str:
        return f'/dla_{session_id}_{self.id}_{position}'

    def get_filename(self) -> str:
        limit = 55

        processed_author = ''
        if self.authors:
            processed_author = self.authors[0]

        processed_author = cast_string_to_single_string(processed_author.lower())
        processed_title = cast_string_to_single_string((self.title or '').lower())

        parts = []
        if processed_author:
            parts.append(processed_author)
        if processed_title:
            parts.append(processed_title)
        filename = '-'.join(parts)

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
            filename = quote(self.doi, safe='')[:limit]

        dt = self.get_issued_datetime()
        if dt:
            filename = f'{filename}-{dt.year}'

        return f'{filename}.pdf'

    def get_formatted_locator(self) -> str:
        parts = []
        if self.authors:
            parts.append(self.get_first_authors(first_n_authors=3))
        journal = self.get_robust_journal()
        if journal:
            parts.extend(['in', journal])
        dt = self.get_formatted_datetime()
        if dt:
            parts.append(f'({dt})')
        if self.get_robust_volume():
            parts.append(self.get_robust_volume())
        if self.get_pages():
            parts.append(self.get_pages())

        return ' '.join(parts)

    def get_pages(self) -> Optional[str]:
        if self.first_page:
            if self.last_page:
                if self.first_page == self.last_page:
                    return f'p. {self.first_page}'
                else:
                    return f'pp. {self.first_page}-{self.last_page}'
            else:
                return f'p. {self.first_page}'
        elif self.last_page:
            return f'p. {self.last_page}'

    def get_referenced_by(self, language):
        if self.ref_by_count:
            return f'**{t("REFERENCED_BY", language=language)}:** {self.ref_by_count}'

    def get_snippet(
        self,
        language: str,
        view_command: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> str:
        snippet = self.generate_body(language=language, with_referenced_by=True, limit=limit)
        if view_command:
            snippet += f'\n{view_command} | {self.get_formatted_filedata()}'
        return snippet

    def get_view(
        self,
        language: str,
        session_id: str,
        bot_external_name: str,
        position: int = 0,
        back_command: Optional[str] = None,
        with_buttons: bool = True,
    ) -> Tuple[str, Optional[List[List[Button]]]]:
        parts = [f'**{self.get_robust_title()}**\n']

        if self.authors:
            parts.append(f'**{t("AUTHORS", language=language)}**: '
                         f'{escape_format(self.get_first_authors(first_n_authors=3))}')
        journal = self.get_robust_journal()
        if journal:
            parts.append(f'**{t("JOURNAL", language=language)}**: {journal}')

        dt = self.get_formatted_datetime()
        if dt:
            parts.append(f'**{t("YEAR", language=language)}**: {dt}')

        if self.downloads_count:
            parts.append(f'**NRank**: {math.log1p(self.downloads_count):.1f}')

        parts.append(f'**Links**: {" - ".join(self.generate_links(bot_external_name))}')

        if self.abstract:
            parts.append(
                f'\n**{t("ABSTRACT", language=language)}**: {escape_format(self.abstract)}',
            )

        if self.tags:
            parts.append(f'\n__{escape_format(", ".join(self.tags))}__')

        buttons = None
        if with_buttons:
            buttons = [[]]
            if back_command:
                buttons[-1].append(
                    Button.inline(
                        text='⬅️',
                        data=back_command
                    )
                )

            # ⬇️ is a mark, Find+F over sources before replacing
            buttons[-1].append(
                Button.inline(
                    text=f'⬇️ {self.get_formatted_filedata()}',
                    data=self.get_download_command(session_id=session_id, position=position),
                )
            )
            if self.ref_by_count:
                buttons[-1].append(
                    Button.inline(
                        text=f'🔗 {self.ref_by_count or ""}',
                        data=f'/r_{session_id}_{self.id}',
                    )
                )
            buttons[-1].append(close_button(session_id))
        return '\n'.join(parts).strip()[:4096], buttons

    def get_view_command(self, session_id: str, message_id: int, parent_view_type: str = 's', position: int = 0) -> str:
        return f'/va{parent_view_type}_{session_id}_{message_id}_{self.id}_{position}'

    def get_robust_journal(self):
        if self.type != 'chapter' and self.type != 'book-chapter':
            return escape_format(self.container_title)

    def get_robust_title(self):
        title = escape_format(self.title or self.doi)
        if self.doi.split('/')[0] in preprints:
            title = '`[P]` ' + title
        if self.type == 'chapter' or self.type == 'book-chapter':
            title += f' in {self.container_title}'
        return title

    def get_robust_volume(self) -> str:
        if self.volume:
            if self.issue:
                return f'vol. {self.volume}({self.issue})'
            else:
                return self.volume
