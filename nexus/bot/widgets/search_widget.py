import logging
import mimetypes
import sys
from typing import Optional

from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from library.telegram.common import close_button
from nexus.bot.application import TelegramApplication
from nexus.meta_api.proto.search_service_pb2 import \
    ScoredDocument as ScoredDocumentPb
from nexus.translations import t
from nexus.views.telegram.base_holder import BaseHolder
from nexus.views.telegram.common import (
    TooLongQueryError,
    encode_query_to_deep_link,
)
from telethon import Button
from telethon.tl.types import (
    DocumentAttributeImageSize,
    InputWebDocument,
)


class BaseSearchWidget:
    """
    Presents markup for the SERP.
    """

    query_tags = ['search']

    def __init__(
        self,
        application: TelegramApplication,
        chat: ChatPb,
        session_id: str,
        request_id: str,
        query: str,
        page: int = 0,
        is_group_mode: bool = False,
    ):
        self.application = application
        self.chat = chat
        self.session_id = session_id
        self.request_id = request_id
        self.query = query
        self.page = page
        self.is_group_mode = is_group_mode

    @classmethod
    async def create(
        cls,
        application: TelegramApplication,
        chat: ChatPb,
        session_id: str,
        request_id: str,
        query: str,
        page: int = 0,
        is_group_mode: bool = False,
    ):
        search_widget_view = cls(
            application=application,
            chat=chat,
            session_id=session_id,
            request_id=request_id,
            query=query,
            page=page,
            is_group_mode=is_group_mode,
        )
        await search_widget_view._acquire_documents()
        return search_widget_view

    async def _acquire_documents(self):
        self._search_response = await self.application.meta_api_client.search(
            index_aliases=self.application.config['application']['index_aliases'],
            query=self.query,
            page=self.page,
            page_size=self.application.config['application']['page_size'],
            request_id=self.request_id,
            session_id=self.session_id,
            user_id=str(self.chat.chat_id),
            language=self.chat.language,
            query_tags=self.query_tags,
        )

    @property
    def query_language(self) -> str:
        return self._search_response.query_language

    @property
    def count(self) -> int:
        return self._search_response.count

    @property
    def has_next(self) -> bool:
        return self._search_response.has_next

    @property
    def scored_documents(self) -> list[ScoredDocumentPb]:
        return self._search_response.scored_documents


class SearchWidget(BaseSearchWidget):
    query_tags = ['search']

    async def render(self, message_id) -> tuple[str, Optional[list]]:
        if len(self.scored_documents) == 0:
            return t('COULD_NOT_FIND_ANYTHING', self.chat.language), [close_button(self.session_id)]

        serp_elements = []
        bot_name = self.application.config['telegram']['bot_name']

        for scored_document in self.scored_documents:
            holder = BaseHolder.create(scored_document.typed_document, scored_document.snippets)
            if self.is_group_mode:
                view_command = holder.get_deep_id_link(bot_name, text='⬇️')
            else:
                view_command = holder.get_view_command(
                    session_id=self.session_id,
                    message_id=message_id,
                    position=scored_document.position,
                )
            serp_elements.append(
                holder
                .view_builder(self.chat.language)
                .add_short_description()
                .add_snippet()
                .add_new_line()
                .add(view_command, escaped=True)
                .add_doi_link(with_leading_pipe=True, text='doi.org')
                .add_references_counter(bot_name=bot_name, with_leading_pipe=True)
                .add_filedata(with_leading_pipe=True)
                .build()
            )

        serp_elements.append(f"__{t('FOUND_N_ITEMS', self.chat.language).format(count=self.count)}__")
        serp = '\n\n'.join(serp_elements)

        if self.is_group_mode:
            try:
                encoded_query = encode_query_to_deep_link(
                    self.query,
                    bot_name,
                )
                serp = (
                    f"{serp}\n\n**{t('DOWNLOAD_AND_SEARCH_MORE', self.chat.language)}: **"
                    f'[@{bot_name}]'
                    f'({encoded_query})'
                )
            except TooLongQueryError:
                serp = (
                    f"{serp}\n\n**{t('DOWNLOAD_AND_SEARCH_MORE', self.chat.language)}: **"
                    f'[@{bot_name}]'
                    f'(https://t.me/{bot_name})'
                )

        promotion_language = self.query_language or self.chat.language
        promo = self.application.promotioner.choose_promotion(promotion_language)
        serp = f'{serp}\n\n{promo}\n'

        buttons = None
        if not self.is_group_mode:
            buttons = []
            if self.has_next or self.page > 0:
                buttons = [
                    Button.inline(
                        text='<<1' if self.page > 1 else ' ',
                        data=f'/search_{self.session_id}_{message_id}_0' if self.page > 1 else '/noop',
                    ),
                    Button.inline(
                        text=f'<{self.page}' if self.page > 0 else ' ',
                        data=f'/search_{self.session_id}_{message_id}_{self.page - 1}'
                        if self.page > 0 else '/noop',
                    ),
                    Button.inline(
                        text=f'{self.page + 2}>' if self.has_next else ' ',
                        data=f'/search_{self.session_id}_{message_id}_{self.page + 1}'
                        if self.has_next else '/noop',
                    )
                ]
            buttons.append(close_button(self.session_id))
        return serp, buttons


class InlineSearchWidget(BaseSearchWidget):
    query_tags = ['inline_search']

    def render(self, builder) -> list:
        items = []
        bot_name = self.application.config['telegram']['bot_name']

        for scored_document in self.scored_documents:
            holder = BaseHolder.create(scored_document.typed_document)
            title = holder.view_builder(self.chat.language).add_icon().add_title(bold=False).limits(140).build()
            description = (
                holder.view_builder(self.chat.language)
                .add_filedata().add_new_line().add_locator(markup=False).limits(160).build()
            )
            response_text = holder.view_builder(self.chat.language).add_short_description().build()
            buttons = holder.buttons_builder(self.chat.language).add_remote_download_button(bot_name=bot_name).build()

            cover_url = holder.get_thumb_url()
            thumb = None
            if cover_url:
                mimetype = mimetypes.guess_type(cover_url)[0]
                if mimetype:
                    thumb = InputWebDocument(
                        url=cover_url,
                        size=-1,
                        mime_type=mimetype,
                        attributes=[DocumentAttributeImageSize(24, 24)]
                    )
            items.append(builder.article(
                title,
                id=str(holder.id),
                text=response_text,
                description=description,
                thumb=thumb,
                buttons=buttons,
            ))

        return items
