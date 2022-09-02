import logging
import re

from library.telegram.base import RequestContext
from library.telegram.common import close_button
from library.telegram.utils import safe_execution
from telethon import events

from .base import BaseHandler


class RankHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile(r'^/rank(?:@\w+)?(.*)?$', re.DOTALL))
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id = self.generate_session_id()
        request_context.add_default_fields(mode='rank', session_id=session_id)

        query = event.pattern_match.group(1).strip()
        bot_name = self.application.config['telegram']['bot_name']
        language = request_context.chat.language

        async with safe_execution(error_log=request_context.error_log, level=logging.DEBUG):
            await event.reply('Coming soon!', buttons=[close_button()])
