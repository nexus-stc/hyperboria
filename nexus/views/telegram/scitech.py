from typing import Optional

from .base_view_builder import (
    BaseButtonsBuilder,
    BaseViewBuilder,
    highlight_markdown,
)


class ScitechButtonsBuilder(BaseButtonsBuilder):
    def add_default_layout(self, bot_name, session_id, position: int = 0):
        return (
            self.add_download_button(session_id, position)
                .add_close_button(session_id)
        )


class ScitechViewBuilder(BaseViewBuilder):
    icon = '📚'

    def add_edition(self, with_brackets=True, bold=False):
        edition = self.document_holder.edition
        if edition:
            if edition.isdigit():
                if edition[-1] == '1':
                    edition += 'st edition'
                elif edition[-1] == '2':
                    edition += 'nd edition'
                elif edition[-1] == '3':
                    edition += 'rd edition'
                else:
                    edition += 'th edition'
        return self.add(edition, with_brackets=with_brackets, bold=bold)

    def add_pages(self):
        if self.document_holder.pages:
            self.add(f'pp. {self.document_holder.pages}')
        return self

    def add_title(self, bold=True):
        title = self.document_holder.title or ''
        if self.document_holder.periodical:
            if title:
                title += f' ({self.document_holder.periodical})'
            else:
                title += self.document_holder.periodical
        elif self.document_holder.volume:
            if title:
                title += f' ({self.document_holder.volume})'
            else:
                title += self.document_holder.volume
        self.add(title, bold=bold)
        self.add_edition(with_brackets=True, bold=bold)
        return self

    def add_snippet(self, on_newline=True):
        snippet = self.document_holder.snippets.get('description')
        if snippet and snippet.highlights:
            if on_newline:
                self.add_new_line()
            self.add(highlight_markdown(snippet), escaped=True)
        return self

    def add_locator(self, first_n_authors=1, markup=True):
        return (
            self.add_authors(first_n_authors=first_n_authors, on_newline=True)
                .add_formatted_datetime()
        )

    def add_filedata(self, with_leading_pipe=False):
        filedata = self.document_holder.get_formatted_filedata()
        if filedata:
            if with_leading_pipe:
                self.add('|')
            self.add(filedata)
        return self

    def add_description(self, limit: Optional[int] = None):
        if self.document_holder.description:
            self.add(self.document_holder.description)
        return self
