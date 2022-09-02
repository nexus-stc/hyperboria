import asyncio
import time

from library.telegram.base import RequestContext
from nexus.translations import t
from telethon import events

from .base import BaseCallbackQueryHandler


def is_earlier_than_2_days(message):
    return time.time() - time.mktime(message.date.timetuple()) < 48 * 60 * 60 - 10


class CloseHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern='^/close(?:_([A-Za-z0-9]+))?(?:_([0-9]+))?$')

    async def handler(self, event, request_context: RequestContext):
        session_id = event.pattern_match.group(1)
        if session_id:
            session_id = session_id.decode()
        request_context.add_default_fields(mode='close')

        target_events = []
        message = await event.get_message()

        if message and is_earlier_than_2_days(message):
            target_events.append(event.answer())
            request_context.statbox(
                action='close',
                message_id=message.id,
                session_id=session_id,
            )
            reply_message = await message.get_reply_message()
            if reply_message and is_earlier_than_2_days(reply_message):
                target_events.append(reply_message.delete())
            target_events.append(message.delete())
        else:
            target_events.append(event.answer(t('DELETION_FORBIDDEN_DUE_TO_AGE')))
        await asyncio.gather(*target_events)
