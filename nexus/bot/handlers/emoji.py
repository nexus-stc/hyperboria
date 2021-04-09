from library.telegram.base import RequestContext
from nexus.nlptools.regex import STICKER_REGEX
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class EmojiHandler(BaseHandler):
    filter = events.NewMessage(
        incoming=True,
        pattern=STICKER_REGEX,
    )

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.statbox(action='show', mode='emoji')
        await event.reply(t('TANKS_BRUH', language=request_context.chat.language))
