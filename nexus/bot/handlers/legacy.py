from library.telegram.base import RequestContext
from nexus.translations import t
from telethon import events

from .base import (
    BaseCallbackQueryHandler,
    BaseHandler,
)


class LegacyHandler(BaseHandler):
    filter = events.NewMessage(
        incoming=True,
        pattern='^/v_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)_([0-9]+)$')

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.statbox(action='show', mode='legacy')
        await event.reply(t('LEGACY', language=request_context.chat.language))


class LegacyCallbackHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(
        pattern='^/dl_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)_([0-9]+)$'
    )

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.statbox(action='show', mode='legacy')
        return await event.answer(t('LEGACY', language=request_context.chat.language))
