import asyncio

from library.telegram.base import RequestContext
from nexus.translations import t
from nexus.views.telegram.common import (
    DecodeDeepQueryError,
    decode_deep_query,
)
from telethon import events

from .search import BaseSearchHandler


class StartHandler(BaseSearchHandler):
    should_reset_last_widget = False
    filter = events.NewMessage(incoming=True, pattern='^/start\\s?(.*)?')

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        raw_query = event.pattern_match.group(1)
        query = None

        request_context.statbox(action='start', mode='start')

        try:
            query = decode_deep_query(raw_query)
        except DecodeDeepQueryError as e:
            request_context.error_log(e, mode='start', raw_query=raw_query)

        if query:
            request_context.statbox(action='query', mode='start', query=query)
            request_message = await self.application.telegram_client.send_message(event.chat, query)
            prefetch_message = await request_message.reply(
                t("SEARCHING", request_context.chat.language),
            )
            self.application.user_manager.last_widget[request_context.chat.chat_id] = prefetch_message.id
            text, buttons = await self.setup_widget(
                request_context=request_context,
                prefetch_message=prefetch_message,
                query=query,
                is_shortpath_enabled=True,
            )
            edit_action = self.application.telegram_client.edit_message(
                request_context.chat.chat_id,
                prefetch_message.id,
                text,
                buttons=buttons,
                link_preview=False,
            )
            await asyncio.gather(
                event.delete(),
                edit_action,
            )
        else:
            request_context.statbox(action='show', mode='start')
            await event.reply(t('HELP', request_context.chat.language))
