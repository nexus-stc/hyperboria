from typing import (
    List,
    Optional,
)

from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from nexus.bot.application import TelegramApplication
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from nexus.translations import t
from nexus.views.telegram.common import close_button
from nexus.views.telegram.registry import parse_typed_document_to_view
from telethon import Button


class DocumentListWidget:
    def __init__(
        self,
        application: TelegramApplication,
        chat: ChatPb,
        typed_documents: List[TypedDocumentPb],
        cmd: str,
        has_next: bool,
        session_id: str,
        message_id: int,
        request_id: str,
        page: int = 0,
        page_size: int = 5,
    ):
        self.application = application
        self.chat = chat
        self.typed_documents = typed_documents
        self.cmd = cmd
        self.has_next = has_next
        self.session_id = session_id
        self.message_id = message_id
        self.request_id = request_id
        self.page = page
        self.page_size = page_size

    async def render(self) -> tuple[str, Optional[list]]:
        if not len(self.typed_documents):
            return t('COULD_NOT_FIND_ANYTHING', language=self.chat.language), [close_button(self.session_id)]

        serp_elements = []
        for position, typed_document in enumerate(self.typed_documents):
            view = parse_typed_document_to_view(typed_document)
            serp_elements.append(
                view.get_snippet(
                    language=self.chat.language,
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
                    data=f'/{self.cmd}_{self.session_id}_{self.message_id}_0'
                    if self.page > 1 else '/noop',
                ),
                Button.inline(
                    text=f'<{self.page}' if self.page > 0 else ' ',
                    data=f'/{self.cmd}_{self.session_id}_{self.message_id}_{self.page - 1}'
                    if self.page > 0 else '/noop',
                ),
                Button.inline(
                    text=f'{self.page + 2}>' if self.has_next else ' ',
                    data=f'/{self.cmd}_{self.session_id}_{self.message_id}_{self.page + 1}'
                    if self.has_next else '/noop',
                )
            ]
        buttons.append(close_button(self.session_id))

        return serp, buttons
