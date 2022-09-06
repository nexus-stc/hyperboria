import logging
import re
import time

from library.telegram.base import RequestContext
from library.telegram.utils import safe_execution
from nexus.views.telegram.base_holder import BaseHolder
from telethon import events

from .base import BaseHandler


class RollHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile(r'^/roll(?:@\w+)?(.*)?$', re.DOTALL))
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        start_time = time.time()

        session_id = self.generate_session_id()
        request_context.add_default_fields(mode='roll', session_id=session_id)
        query = event.pattern_match.group(1).strip()
        bot_name = self.application.config['telegram']['bot_name']
        language = request_context.chat.language

        meta_search_response = await self.application.meta_api_client.meta_search(
            index_aliases=['scimag', 'scitech'],
            languages={request_context.chat.language: 1.0} if request_context.chat.language else None,
            query=query,
            collectors=[{'reservoir_sampling': {'limit': 1}}],
            session_id=session_id,
            request_id=request_context.request_id,
            user_id=str(request_context.chat.chat_id),
            query_tags=['roll'],
            skip_cache_loading=True,
            skip_cache_saving=True,
        )
        random_documents = meta_search_response.collector_outputs[0].reservoir_sampling.random_documents

        if random_documents:
            holder = BaseHolder.create_from_document(random_documents[0])
            promo = self.application.promotioner.choose_promotion(language)
            view = holder.view_builder(language).add_view(bot_name=bot_name).add_new_line(2).add(promo, escaped=True).build()
            buttons_builder = holder.buttons_builder(language)

            if request_context.is_group_mode():
                buttons_builder.add_remote_download_button(bot_name=bot_name)
            else:
                buttons_builder.add_download_button(session_id)
                buttons_builder.add_close_button(session_id)

            request_context.statbox(action='show', duration=time.time() - start_time)
            await event.respond(view, buttons=buttons_builder.build())
        async with safe_execution(is_logging_enabled=False):
            await event.delete()
