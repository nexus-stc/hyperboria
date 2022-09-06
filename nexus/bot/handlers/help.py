from library.telegram.base import RequestContext
from nexus.translations import t
from telethon import (
    Button,
    events,
)

from .base import BaseHandler


class HelpHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/help(@[A-Za-z0-9_]+)?$')
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.statbox(action='show', mode='help')
        if event.is_group or event.is_channel:
            await event.reply(t('HELP_FOR_GROUPS', request_context.chat.language), buttons=Button.clear())
        else:
            await event.reply(t('HELP', request_context.chat.language), buttons=Button.clear())
