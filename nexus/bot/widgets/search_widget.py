from typing import Optional

from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from nexus.bot.application import TelegramApplication
from nexus.meta_api.proto.search_service_pb2 import \
    ScoredDocument as ScoredDocumentPb
from nexus.translations import t
from nexus.views.telegram.common import (
    TooLongQueryError,
    close_button,
    encode_query_to_deep_link,
)
from nexus.views.telegram.registry import parse_typed_document_to_view
from telethon import Button


class SearchWidget:
    """
    Presents markup for the SERP.
    """
    def __init__(
        self,
        application: TelegramApplication,
        chat: ChatPb,
        session_id: str,
        message_id: int,
        request_id: str,
        query: str,
        page: int = 0,
        is_group_mode: bool = False,
    ):
        self.application = application
        self.chat = chat
        self.session_id = session_id
        self.message_id = message_id
        self.request_id = request_id
        self.query = query
        self.page = page
        self.is_group_mode = is_group_mode

    @staticmethod
    async def create(
        application: TelegramApplication,
        chat: ChatPb,
        session_id: str,
        message_id: int,
        request_id: str,
        query: str,
        page: int = 0,
        is_group_mode: bool = False,
    ) -> 'SearchWidget':
        search_widget_view = SearchWidget(
            application=application,
            chat=chat,
            session_id=session_id,
            message_id=message_id,
            request_id=request_id,
            query=query,
            page=page,
            is_group_mode=is_group_mode,
        )
        await search_widget_view._acquire_documents()
        return search_widget_view

    async def _acquire_documents(self):
        self._search_response = await self.application.meta_api_client.search(
            schemas=self.application.config['application']['schemas'],
            query=self.query,
            page=self.page,
            page_size=self.application.config['application']['page_size'],
            request_id=self.request_id,
            session_id=self.session_id,
            user_id=str(self.chat.chat_id),
            language=self.chat.language,
        )

    @property
    def has_next(self) -> bool:
        return self._search_response.has_next

    @property
    def scored_documents(self) -> list[ScoredDocumentPb]:
        return self._search_response.scored_documents

    async def render(self) -> tuple[str, Optional[list]]:
        if not len(self.scored_documents):
            return t('COULD_NOT_FIND_ANYTHING', language=self.chat.language), [close_button(self.session_id)]

        serp_elements = []
        bot_external_name = self.application.config['telegram']['bot_external_name']

        for scored_document in self.scored_documents:
            view = parse_typed_document_to_view(scored_document.typed_document)
            if not self.is_group_mode:
                view_command = view.get_view_command(
                    session_id=self.session_id,
                    message_id=self.message_id,
                    position=scored_document.position,
                )
            else:
                view_command = view.get_deep_link(bot_external_name, text='⬇️')
            serp_elements.append(
                view.get_snippet(
                    language=self.chat.language,
                    view_command=view_command,
                    limit=512 + 128,
                )
            )
        serp = '\n\n'.join(serp_elements)

        if self.is_group_mode:
            try:
                encoded_query = encode_query_to_deep_link(
                    self.query,
                    bot_external_name,
                )
                serp = (
                    f"{serp}\n\n**{t('DOWNLOAD_AND_SEARCH_MORE', language=self.chat.language)}: **"
                    f'[@{bot_external_name}]'
                    f'({encoded_query})'
                )
            except TooLongQueryError:
                serp = (
                    f"{serp}\n\n**{t('DOWNLOAD_AND_SEARCH_MORE', language=self.chat.language)}: **"
                    f'[@{bot_external_name}]'
                    f'(https://t.me/{bot_external_name})'
                )

        if not self.is_group_mode:
            promo = self.application.promotioner.choose_promotion(language=self.chat.language).format(
                related_channel=self.application.config['telegram']['related_channel'],
            )
            serp = f'{serp}\n\n{promo}\n'

        buttons = None
        if not self.is_group_mode:
            buttons = []
            if self.has_next or self.page > 0:
                buttons = [
                    Button.inline(
                        text='<<1' if self.page > 1 else ' ',
                        data=f'/search_{self.session_id}_{self.message_id}_0' if self.page > 1 else '/noop',
                    ),
                    Button.inline(
                        text=f'<{self.page}' if self.page > 0 else ' ',
                        data=f'/search_{self.session_id}_{self.message_id}_{self.page - 1}'
                        if self.page > 0 else '/noop',
                    ),
                    Button.inline(
                        text=f'{self.page + 2}>' if self.has_next else ' ',
                        data=f'/search_{self.session_id}_{self.message_id}_{self.page + 1}'
                        if self.has_next else '/noop',
                    )
                ]
            buttons.append(close_button(self.session_id))

        return serp, buttons
