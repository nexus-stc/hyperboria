import asyncio

from library.telegram.base import RequestContext
from nexus.bot.exceptions import UnknownFileFormatError
from nexus.translations import t
from nexus.views.telegram.common import close_button
from telethon import events

from .base import BaseHandler


class SubmitHandler(BaseHandler):
    filter = events.NewMessage(func=lambda e: e.document, incoming=True)
    is_group_handler = False
    writing_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id = self.generate_session_id()

        request_context.add_default_fields(session_id=session_id)
        request_context.statbox(action='show', mode='submit')

        if event.document.mime_type != 'application/pdf':
            request_context.statbox(action='unknown_file_format')
            request_context.error_log(UnknownFileFormatError(format=event.document.mime_type))
            return await asyncio.gather(
                event.reply(
                    t('UNKNOWN_FILE_FORMAT_ERROR', language=request_context.chat.language),
                    buttons=[close_button()],
                ),
                event.delete(),
            )

        return await asyncio.gather(
            self.application.hub_client.submit(
                telegram_document=bytes(event.document),
                telegram_file_id=event.file.id,
                chat=request_context.chat,
                request_id=request_context.request_id,
                session_id=session_id,
                bot_name=request_context.bot_name,
            ),
            event.delete(),
        )
