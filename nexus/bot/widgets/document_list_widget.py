from typing import Optional

from idm.api2.proto.chats_service_pb2 import ChatData as Chat
from nexus.bot.application import TelegramApplication
from nexus.meta_api.proto.meta_search_service_pb2 import \
    ScoredDocument as ScoredDocumentPb
from nexus.translations import t
from nexus.views.telegram.common import close_button
from nexus.views.telegram.registry import parse_typed_document_to_view
from telethon import Button


class DocumentListWidget:
    def __init__(
        self,
        application: TelegramApplication,
        chat: Chat,
        session_id: str,
        message_id: int,
        request_id: str,
        referencing_to: int,
        page: int = 0,
    ):
        self.application = application
        self.chat = chat
        self.session_id = session_id
        self.message_id = message_id
        self.request_id = request_id
        self.referencing_to = referencing_to
        self.page = page

    @staticmethod
    async def create(
        application: TelegramApplication,
        chat: Chat,
        session_id: str,
        message_id: int,
        request_id: str,
        referencing_to: int,
        page: int = 0,
    ) -> 'DocumentListWidget':
        document_list_view = DocumentListWidget(
            application=application,
            chat=chat,
            session_id=session_id,
            message_id=message_id,
            request_id=request_id,
            referencing_to=referencing_to,
            page=page,
        )
        await document_list_view._acquire_documents()
        return document_list_view

    async def _acquire_documents(self):
        typed_document_pb = await self.application.meta_api_client.get(
            schema='scimag',
            document_id=self.referencing_to,
            position=0,
            request_id=self.request_id,
            session_id=self.session_id,
            user_id=self.chat.id,
        )
        self._response = await self.application.meta_api_client.search(
            schemas=('scimag',),
            query=f'references:"{typed_document_pb.scimag.doi}"',
            page=self.page,
            request_id=self.request_id,
            session_id=self.session_id,
            user_id=self.chat.id,
        )

    @property
    def has_next(self) -> bool:
        return self._response.has_next

    @property
    def scored_documents(self) -> list[ScoredDocumentPb]:
        return self._response.scored_documents

    async def render(self) -> tuple[str, Optional[list]]:
        if not len(self.scored_documents):
            return t('COULD_NOT_FIND_ANYTHING', language=self.chat.language), [close_button(self.session_id)]

        serp_elements = [
            f'Linked to: {self.referencing_to}',
        ]
        for scored_document in self.scored_documents:
            view = parse_typed_document_to_view(scored_document.typed_document)
            view_command = view.get_view_command(
                session_id=self.session_id,
                message_id=self.message_id,
                parent_view_type='r',
                position=scored_document.position,
            )
            serp_elements.append(
                view.get_snippet(
                    language=self.chat.language,
                    view_command=view_command,
                    limit=512 + 128,
                )
            )

        promo = self.application.promotioner.choose_promotion(language=self.chat.language).format(
            related_channel=self.application.config['telegram']['related_channel'],
        )
        serp_elements.append(promo)
        serp = '\n\n'.join(serp_elements)

        buttons = []
        if self.has_next or self.page > 0:
            buttons = [
                Button.inline(
                    text='<<1' if self.page > 1 else ' ',
                    data=f'/rp_{self.session_id}_{self.message_id}_{self.referencing_to}_0'
                    if self.page > 1 else '/noop',
                ),
                Button.inline(
                    text=f'<{self.page}' if self.page > 0 else ' ',
                    data=f'/rp_{self.session_id}_{self.message_id}_{self.referencing_to}_{self.page - 1}'
                    if self.page > 0 else '/noop',
                ),
                Button.inline(
                    text=f'{self.page + 2}>' if self.has_next else ' ',
                    data=f'/rp_{self.session_id}_{self.message_id}_{self.referencing_to}_{self.page + 1}'
                    if self.has_next else '/noop',
                )
            ]
        buttons.append(close_button(self.session_id))

        return serp, buttons
