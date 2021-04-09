import asyncio

from library.telegram.base import RequestContext
from telethon import events

from .base import BaseCallbackQueryHandler


class CloseHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern='^/close(?:_([A-Za-z0-9]+))?(?:_([0-9]+))?$')

    async def handler(self, event, request_context: RequestContext):
        session_id = event.pattern_match.group(1)
        if session_id:
            session_id = session_id.decode()
        request_context.add_default_fields(mode='close')

        target_events = [event.answer()]
        message = await event.get_message()

        if message:
            request_context.statbox(
                action='close',
                message_id=message.id,
                session_id=session_id,
            )
            reply_message = await message.get_reply_message()
            if reply_message:
                target_events.append(reply_message.delete())
            target_events.append(message.delete())
        await asyncio.gather(*target_events)
