from typing import (
    Iterable,
    List,
    Optional,
    Tuple,
)
from urllib.parse import quote

from izihawa_utils.common import (
    filter_none,
    is_essential,
)
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb
from nexus.nlptools.utils import (
    cast_string_to_single_string,
    despace,
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


class ScitechView(BaseView, AuthorMixin, DoiMixin, FileMixin, IssuedAtMixin):
    icon = '📚'
    schema = 'scitech'

    def __init__(self, document_pb: ScitechPb, duplicates: Optional[Iterable[ScitechPb]] = tuple()):
        self.document_pb = document_pb
        self.duplicates = [ScitechView(
            document_pb=document_pb,
        ) for document_pb in duplicates]

    def generate_body(self, language: str, limit: Optional[int] = None) -> str:
        head = self.icon
        title = self.get_robust_title()
        if title:
            head += f' **{title}**'

        doi = None
        if self.doi:
            doi = f'**DOI:** {self.get_doi_link()}'

        locator = self.get_formatted_locator()

        caption = '\n'.join(filter_none([head, doi, locator], predicate=is_essential))
        if limit and len(caption) > limit:
            shorten_title = title[:limit]
            shorten_title = shorten_title[:max(32, shorten_title.rfind(' '))]
            caption = f'{self.icon} **{shorten_title}**'

        return caption

    def get_cover_url(self):
        if self.cu:
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

    def get_download_command(self, session_id: str, position: int = 0) -> str:
        return f'/dlb_{session_id}_{self.id}_{position}'

    def get_extension(self):
        return self.extension

    def get_filename(self) -> str:
        limit = 55

        processed_author = cast_string_to_single_string(self.get_first_authors(et_al=False).lower())
        processed_title = cast_string_to_single_string(self.get_robust_title().lower())

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
            if self.doi:
                filename = quote(self.doi, safe='')
            else:
                filename = self.md5

        dt = self.get_issued_datetime()
        if dt:
            filename = f'{filename}-{dt.year}'

        return f'{filename}.{self.get_extension()}'

    def get_formatted_locator(self) -> str:
        parts = []
        if self.authors:
            parts.append(self.get_first_authors(first_n_authors=3))
        dt = self.get_issued_datetime()
        if dt:
            parts.append(f'({dt.year})')
        if self.pages:
            parts.append(f'pp. {self.pages}')

        return escape_format(' '.join(parts)) or ''

    def get_robust_title(self):
        title = self.title or ''
        if self.volume:
            if title:
                title += f' ({self.volume})'
            else:
                title += self.volume
        return escape_format(title)

    def get_snippet(
        self,
        language: str,
        view_command: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> str:
        snippet = self.generate_body(language=language, limit=limit)
        if view_command:
            snippet += f'\n{view_command} | {self.get_formatted_filedata(show_format=not self.has_duplicates)}'
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
        cover_url = self.get_cover_url()
        if cover_url:
            # There is an invisible character inside []!
            parts[-1] = f'[​]({cover_url})' + parts[-1]

        if self.authors:
            parts.append(f'**{t("AUTHORS", language=language)}**: '
                         f'{escape_format(self.get_first_authors(first_n_authors=3))}')
        dt = self.get_issued_datetime()
        if dt:
            parts.append(f'**{t("YEAR", language=language)}**: {dt.year}')
        if self.edition:
            parts.append(f'**{t("EDITION", language=language)}**: '
                         f'{escape_format(self.edition)}')

        parts.append(f'**Links**: {" - ".join(self.generate_links(bot_external_name))}')

        if self.description:
            parts.append(
                f'\n**{t("DESCRIPTION", language=language)}**:\n'
                f'{escape_format(despace(self.description))}',
            )

        if self.tags:
            parts.append(f'\n__{escape_format(", ".join(self.tags))}__')

        buttons = None
        if with_buttons:
            buttons = [[]]
            # Plain layout
            if not self.duplicates:
                if back_command:
                    buttons[-1].append(Button.inline(
                        text='⬅️',
                        data=back_command
                    ))
                buttons[-1].extend([
                    Button.inline(
                        text=f'⬇️ {self.get_formatted_filedata(show_language=False)}',
                        data=self.get_download_command(session_id=session_id, position=position),
                    ),
                    close_button(session_id),
                ])
            else:
                buttons = [[]]
                for view in [self] + self.duplicates:
                    filedata = view.get_formatted_filedata(show_language=False, show_filesize=True)
                    if len(buttons[-1]) >= 2:
                        buttons.append([])
                    # ⬇️ is a mark, Find+F over sources before replacing
                    buttons[-1].append(
                        Button.inline(
                            text=f'⬇️ {filedata}',
                            data=view.get_download_command(session_id=session_id, position=position),
                        )
                    )
                if len(buttons[-1]) == 1:
                    buttons[-1].append(Button.inline(
                        text=' ',
                        data='/noop',
                    ))
                buttons.append([])
                if back_command:
                    buttons[-1].append(Button.inline(
                        text='⬅️',
                        data=back_command,
                    ))
                buttons[-1].append(close_button(session_id))

        return '\n'.join(parts).strip()[:4096], buttons

    def get_view_command(self, session_id: str, message_id: int, position: int = 0) -> str:
        return f'/vb_{session_id}_{message_id}_{self.id}_{position}'
