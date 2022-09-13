import math

from izihawa_types.safecast import safe_int
from telethon import Button

from .base_view_builder import (
    BaseButtonsBuilder,
    BaseViewBuilder,
    highlight_markdown,
)
from .common import (
    TooLongQueryError,
    encode_query_to_deep_link,
)

preprints = {'10.1101', '10.21203'}


class ScimagButtonsBuilder(BaseButtonsBuilder):
    def add_linked_search_button(self, bot_name):
        if self.document_holder.referenced_by_count:
            try:
                self.buttons[-1].append(
                    Button.url(
                        text=f'🔗 {self.document_holder.referenced_by_count or ""}',
                        url=encode_query_to_deep_link(f'refs:{self.document_holder.doi}', bot_name=bot_name),
                    )
                )
            except TooLongQueryError:
                pass
        return self

    def add_journal_search(self, bot_name):
        try:
            issn_query = [f'issn:{issn}' for issn in self.document_holder.issns[:2]]
            if issn_query:
                issn_query.append('order_by:date')
                issn_query = ' '.join(issn_query)
                self.buttons[-1].append(
                    Button.url(
                        text='📰',
                        url=encode_query_to_deep_link(issn_query, bot_name=bot_name),
                    )
                )
        except TooLongQueryError:
            pass
        return self

    def add_default_layout(self, bot_name, session_id, position: int = 0):
        return (
            self.add_download_button(session_id, position)
                .add_linked_search_button(bot_name)
                .add_journal_search(bot_name)
                .add_close_button(session_id)
        )


class ScimagViewBuilder(BaseViewBuilder):
    icon = '🔬'
    icons = {
        'book': '📚',
        'monograph': '📚',
        'chapter': '🔖',
        'book-chapter': '🔖',
    }

    def is_preprint(self):
        return self.document_holder.doi.split('/')[0] in preprints

    def add_icon(self):
        return self.add(self.icons.get(self.document_holder.type, self.icon))

    def add_pages(self):
        if self.document_holder.first_page:
            if self.document_holder.last_page:
                if self.document_holder.first_page == self.document_holder.last_page:
                    self.add(f'p. {self.document_holder.first_page}')
                else:
                    self.add(f'pp. {self.document_holder.first_page}-{self.document_holder.last_page}')
            else:
                self.add(f'p. {self.document_holder.first_page}')
        elif self.document_holder.last_page:
            self.add(f'p. {self.document_holder.last_page}')
        return self

    def add_container(self, bold=False, italic=False):
        if self.document_holder.container_title:
            self.add('in')
            self.add(self.document_holder.container_title, bold=bold, italic=italic)
        return self

    def add_volume(self):
        if self.document_holder.volume:
            if self.document_holder.issue:
                self.add(f'vol. {self.document_holder.volume}({self.document_holder.issue})')
            else:
                if safe_int(self.document_holder.volume):
                    self.add(f'vol. {self.document_holder.volume}')
                else:
                    self.add(self.document_holder.volume)
        return self

    def add_title(self, bold=True):
        self.add(self.document_holder.title or self.document_holder.doi, bold=bold)
        return self

    def add_snippet(self, on_newline=True):
        snippet = self.document_holder.snippets.get('abstract')
        if snippet and snippet.highlights:
            if on_newline:
                self.add_new_line()
            self.add(highlight_markdown(snippet), escaped=True)
        return self

    def add_locator(self, first_n_authors=1, markup=True):
        return (
            self.add_authors(first_n_authors=first_n_authors)
                .add_container(italic=markup)
                .add_formatted_datetime()
                .add_pages()
        )

    def add_filedata(self, with_leading_pipe=False):
        filedata = self.document_holder.get_formatted_filedata()
        if filedata:
            if with_leading_pipe:
                self.add('|')
            self.add(filedata)
        return self

    def add_description(self):
        if self.document_holder.abstract:
            self.add(self.document_holder.abstract)
        return self

    def add_stats(self, end_newline=True):
        if self.document_holder.page_rank:
            star_rank = int(round(math.log10(self.document_holder.page_rank + 1) + 2)) * '⭐'
            if star_rank:
                self.add(f'**Rank**: {star_rank}', escaped=True)
            else:
                self.add(f'**Rank**: ❔', escaped=True)
            if end_newline:
                self.add_new_line()
        return self
