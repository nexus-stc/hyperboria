import asyncio
import re
import time

from library.telegram.base import RequestContext
from nexus.bot.widgets.profile_widget import ProfileWidget
from nexus.views.telegram.base_holder import BaseHolder
from nexus.views.telegram.document_list_widget import DocumentListWidget
from telethon import events
from telethon.tl.types import PeerChannel

from .base import BaseHandler


class ProfileHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile('^/profile'))
    is_group_handler = True
    should_reset_last_widget = False
    stop_propagation = True

    async def handler(self, event, request_context: RequestContext):
        request_context.add_default_fields(mode='profile')
        profile_user_id = None
        profile_reply_message = None

        target_events = []

        if request_context.is_personal_mode():
            profile_user_id = request_context.chat.chat_id
            target_events.append(event.delete())
        else:
            reply_message = await event.get_reply_message()
            if reply_message:
                target_events.append(event.delete())
                if not isinstance(reply_message.from_id, PeerChannel):
                    profile_user_id = reply_message.from_id.user_id
                    profile_reply_message = reply_message
            else:
                if not isinstance(event.from_id, PeerChannel):
                    profile_user_id = event.from_id.user_id
                    profile_reply_message = event
                else:
                    target_events.append(event.delete())

        if profile_user_id is None:
            return await asyncio.gather(*target_events)

        request_context.statbox(
            action='show',
            profile_user_id=profile_user_id,
        )

        profile = await self.application.idm_client.get_profile(chat_id=profile_user_id, last_n_documents=300)
        profile_widget = ProfileWidget(
            application=self.application,
            request_context=request_context,
            profile=profile,
        )
        rendered_widget, buttons = await profile_widget.render()
        if profile_reply_message:
            target_events.append(profile_reply_message.reply(rendered_widget, buttons=buttons, link_preview=False))
        else:
            target_events.append(event.reply(rendered_widget, buttons=buttons, link_preview=False))
        return asyncio.gather(*target_events)


class DigestHandler(BaseHandler):
    filter = events.CallbackQuery(pattern=re.compile('^/digest$'))
    should_reset_last_widget = False

    async def handler(self, event, request_context: RequestContext):
        bot_name = self.application.config['telegram']['bot_name']
        session_id = self.generate_session_id()

        request_context.add_default_fields(mode='digest', session_id=session_id)

        profile = await self.application.idm_client.get_profile(
            request_context.chat.chat_id,
            last_n_documents=100,
        )
        query = []
        for series in profile.most_popular_series:
            for issn in series.issns:
                query.append(f'issn:{issn}')
        for tag in profile.most_popular_tags:
            query.append(f'tag:"{tag}"')
        query.append(f'+issued_at:[{int(time.time() - 3600 * 24 * 7)} TO {int(time.time())}]')
        for document in profile.downloaded_documents:
            query.append(f'-id:{document.id}')
        query = ' '.join(query)

        request_context.statbox(
            action='query',
            query=query,
        )

        search_response = await self.application.meta_api_client.meta_search(
            index_aliases=['scimag'],
            query=query,
            collectors=[{'top_docs': {'limit': 5}}],
            user_id=str(request_context.chat.chat_id),
            query_tags=['digest'],
            session_id=session_id,
            request_id=request_context.request_id,
        )
        document_holders = [
            BaseHolder.create_from_document(scored_document)
            for scored_document in search_response.collector_outputs[0].top_docs.scored_documents
        ]
        chat = await self.application.idm_client.get_chat(chat_id=request_context.chat.chat_id)

        document_list_widget = DocumentListWidget(
            chat=chat,
            document_holders=document_holders,
            bot_name=bot_name,
            header='✨ Nexus Discovery ✨',
        )

        view, buttons = await document_list_widget.render()

        await event.reply(
            view,
            buttons=buttons,
            link_preview=False,
        )

