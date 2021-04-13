from library.telegram.base import RequestContext
from nexus.bot.widgets.document_list_widget import DocumentListWidget
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class TopMissedHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/tm$')
    is_group_handler = False
    should_reset_last_widget = False

    async def do_request(self, request_context: RequestContext, session_id: str, message_id: int, page: int):
        response = await self.application.meta_api_client.top_missed(
            page=page,
            page_size=10,
            session_id=session_id,
            request_id=request_context.request_id,
        )
        document_list_widget = DocumentListWidget(
            application=self.application,
            chat=request_context.chat,
            typed_documents=response.typed_documents,
            cmd='tm',
            has_next=response.has_next,
            session_id=session_id,
            message_id=message_id,
            request_id=request_context.request_id,
            page=page,
        )
        serp, buttons = await document_list_widget.render()
        return await self.application.telegram_client.edit_message(
            request_context.chat.chat_id,
            message_id,
            serp,
            buttons=buttons,
            link_preview=False,
        )

    async def handler(self, event, request_context: RequestContext):
        session_id = self.generate_session_id()
        request_context.add_default_fields(mode='top_missed', session_id=session_id)
        request_context.statbox()

        prefetch_message = await event.reply(t("SEARCHING", language=request_context.chat.language))
        message_id = prefetch_message.id

        return await self.do_request(
            request_context=request_context,
            session_id=session_id,
            message_id=message_id,
            page=0,
        )
