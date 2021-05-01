import asyncio
import re

from library.telegram.base import RequestContext
from telethon import events

from .base import BaseHandler


class RollHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile('^/roll(@[A-Za-z0-9_]+)?$', re.DOTALL))
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id = self.generate_session_id()
        request_context.add_default_fields(mode='roll', session_id=session_id)
        request_context.statbox(action='show')

        roll_response_pb = await self.application.meta_api_client.roll(
            language=request_context.chat.language,
            session_id=session_id,
            request_id=request_context.request_id,
            user_id=str(request_context.chat.chat_id),
        )
        scitech_view = await self.resolve_scitech(
            document_id=roll_response_pb.document_id,
            position=0,
            request_context=request_context,
            session_id=session_id,
        )
        view, buttons = scitech_view.get_view(
            language=request_context.chat.language,
            session_id=session_id,
            bot_external_name=self.application.config['telegram']['bot_external_name'],
        )
        actions = [
            self.application.telegram_client.send_message(
                request_context.chat.chat_id,
                view,
                buttons=buttons,
            ),
            event.delete(),
        ]
        return await asyncio.gather(*actions)
