import re

from library.telegram.base import RequestContext
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class CopyrightHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile('^/copyright\\s?(.*)', re.DOTALL))

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        query = event.pattern_match.group(1)
        if query:
            request_context.statbox(
                action='show',
                mode='copyright',
                query=query,
            )
            await self.application.telegram_client.forward_messages(
                self.application.config['telegram']['copyright_infringement_account'],
                event.message,
            )
            await event.reply(t(
                'COPYRIGHT_INFRINGEMENT_ACCEPTED',
                language=request_context.chat.language,
            ))
        else:
            request_context.statbox(action='show', mode='copyright')
            await event.reply(t('COPYRIGHT_DESCRIPTION', language=request_context.chat.language,))
