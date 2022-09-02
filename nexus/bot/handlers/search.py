import asyncio
import re
import time
from abc import ABC
from typing import Union

from grpc import StatusCode
from grpc.experimental.aio import AioRpcError
from library.telegram.base import RequestContext
from library.telegram.common import close_button
from library.telegram.utils import safe_execution
from nexus.bot.exceptions import BannedUserError
from nexus.bot.widgets.search_widget import (
    InlineSearchWidget,
    SearchWidget,
)
from nexus.translations import t
from nexus.views.telegram.base_holder import BaseHolder
from nexus.views.telegram.common import encode_deep_query
from telethon import (
    Button,
    events,
)
from telethon.tl.types import InlineQueryPeerTypeSameBotPM

from .base import (
    BaseCallbackQueryHandler,
    BaseHandler,
)


class BaseSearchHandler(BaseHandler, ABC):
    async def setup_widget(
        self,
        request_context: RequestContext,
        prefetch_message,
        query: str,
        is_shortpath_enabled: bool = False,
    ) -> tuple[str, list[Union[list[Button]], list[Button]]]:
        session_id = self.generate_session_id()
        message_id = prefetch_message.id
        request_context.add_default_fields(
            is_group_mode=request_context.is_group_mode(),
            mode='search',
            session_id=session_id,
        )
        start_time = time.time()
        language = request_context.chat.language
        bot_name = self.application.config['telegram']['bot_name']

        try:
            search_widget = await SearchWidget.create(
                application=self.application,
                chat=request_context.chat,
                session_id=session_id,
                request_id=request_context.request_id,
                query=query,
                is_group_mode=request_context.is_group_mode(),
            )
        except AioRpcError as e:
            if e.code() == StatusCode.INVALID_ARGUMENT:
                return t('INVALID_SYNTAX_ERROR', language).format(
                    too_difficult_picture_url=self.application.config['application'].get('too_difficult_picture_url', ''),
                ), [close_button()]
            elif e.code() == StatusCode.CANCELLED:
                return t('MAINTENANCE', language).format(
                    maintenance_picture_url=self.application.config['application'].get('maintenance_picture_url', ''),
                ), [close_button()],
            request_context.error_log(e)
            raise e

        request_context.statbox(
            action='documents_retrieved',
            duration=time.time() - start_time,
            query=query,
            page=0,
            scored_documents=len(search_widget.scored_documents),
        )

        if len(search_widget.scored_documents) == 1 and is_shortpath_enabled:
            holder = BaseHolder.create(search_widget.scored_documents[0].typed_document)
            view = holder.view_builder(language).add_view(bot_name=bot_name).build()
            buttons = holder.buttons_builder(language).add_default_layout(
                bot_name=bot_name,
                session_id=session_id,
                position=0,
            ).build()
            return view, buttons

        return await search_widget.render(message_id=message_id)


class SearchHandler(BaseSearchHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile(r'^(/search(?:@\w+)?\s+)?(.*)', flags=re.DOTALL))
    is_group_handler = True
    should_reset_last_widget = False
    is_subscription_required_for_handler = True

    def check_search_ban_timeout(self, user_id: str):
        ban_timeout = self.application.user_manager.check_search_ban_timeout(user_id=user_id)
        if ban_timeout:
            raise BannedUserError(ban_timeout=ban_timeout)
        self.application.user_manager.add_search_time(user_id=user_id, search_time=time.time())

    def parse_pattern(self, event: events.ChatAction):
        search_prefix = event.pattern_match.group(1)
        query = event.pattern_match.group(2).strip()

        return search_prefix, query

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        language = request_context.chat.language
        try:
            self.check_search_ban_timeout(user_id=str(request_context.chat.chat_id))
        except BannedUserError as e:
            request_context.error_log(e)
            async with safe_execution(error_log=request_context.error_log):
                return await event.reply(t('BANNED_FOR_SECONDS', language).format(
                    seconds=e.ban_timeout,
                    reason=t('BAN_MESSAGE_TOO_MANY_REQUESTS', language),
                ))
        search_prefix, query = self.parse_pattern(event)

        if request_context.is_group_mode() and not search_prefix:
            return
        if request_context.is_personal_mode() and search_prefix:
            query = event.raw_text

        prefetch_message = await event.reply(
            t("SEARCHING", language),
        )
        self.application.user_manager.last_widget[request_context.chat.chat_id] = prefetch_message.id
        try:
            text, buttons = await self.setup_widget(
                request_context=request_context,
                prefetch_message=prefetch_message,
                query=query,
                is_shortpath_enabled=True,
            )
            return await self.application.telegram_client.edit_message(
                request_context.chat.chat_id,
                prefetch_message.id,
                text,
                buttons=buttons,
                link_preview=False,
            )
        except (AioRpcError, asyncio.CancelledError) as e:
            await asyncio.gather(
                event.delete(),
                prefetch_message.delete(),
            )
            raise e


class InlineSearchHandler(BaseSearchHandler):
    filter = events.InlineQuery()
    stop_propagation = False

    async def handler(self, event, request_context: RequestContext):
        if event.query.peer_type == InlineQueryPeerTypeSameBotPM():
            await event.answer()
            return

        builder = event.builder
        session_id = self.generate_session_id()

        try:
            if len(event.text) <= 3:
                await event.answer([])
                raise events.StopPropagation()
            inline_search_widget = await InlineSearchWidget.create(
                application=self.application,
                chat=request_context.chat,
                session_id=session_id,
                request_id=request_context.request_id,
                query=event.text,
                is_group_mode=request_context.is_group_mode(),
            )
            items = inline_search_widget.render(builder=builder)
            encoded_query = encode_deep_query(event.text)
            if len(encoded_query) < 32:
                await event.answer(
                    items,
                    private=True,
                    switch_pm=self.application.config['telegram']['bot_name'],
                    switch_pm_param=encoded_query,
                )
            else:
                await event.answer(items)
        except AioRpcError as e:
            if e.code() == StatusCode.INVALID_ARGUMENT or e.code() == StatusCode.CANCELLED:
                await event.answer([])
            raise e
        raise events.StopPropagation()


class SearchEditHandler(BaseSearchHandler):
    filter = events.MessageEdited(incoming=True, pattern=re.compile(r'^(/search(?:@\w+)\s+)?(.*)', flags=re.DOTALL))
    is_group_handler = True
    should_reset_last_widget = False

    def parse_pattern(self, event: events.ChatAction):
        search_prefix = event.pattern_match.group(1)
        query = event.pattern_match.group(2).strip()
        return search_prefix, query

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        search_prefix, query = self.parse_pattern(event)
        request_context.add_default_fields(mode='search_edit')

        if request_context.is_group_mode() and not search_prefix:
            return
        if request_context.is_personal_mode() and search_prefix:
            query = event.raw_text

        for next_message in await self.get_last_messages_in_chat(event):
            if next_message.is_reply and event.id == next_message.reply_to_msg_id:
                request_context.statbox(action='resolved')
                text, buttons = await self.setup_widget(
                    request_context=request_context,
                    prefetch_message=next_message,
                    query=query,
                )
                return await self.application.telegram_client.edit_message(
                    request_context.chat.chat_id,
                    next_message.id,
                    text,
                    buttons=buttons,
                    link_preview=False,
                )
        return await event.reply(
            t('REPLY_MESSAGE_HAS_BEEN_DELETED', request_context.chat.language),
        )


class SearchPagingHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern='^/search_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)$')
    should_reset_last_widget = False

    def parse_pattern(self, event: events.ChatAction):
        session_id = event.pattern_match.group(1).decode()
        message_id = int(event.pattern_match.group(2).decode())
        page = int(event.pattern_match.group(3).decode())

        return session_id, message_id, page

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id, message_id, page = self.parse_pattern(event)

        request_context.add_default_fields(mode='search_paging', session_id=session_id)
        start_time = time.time()

        message = await event.get_message()
        if not message:
            return await event.answer()

        reply_message = await message.get_reply_message()
        if not reply_message:
            return await event.respond(
                t('REPLY_MESSAGE_HAS_BEEN_DELETED', request_context.chat.language),
            )

        query = reply_message.raw_text.replace(f'@{self.application.config["telegram"]["bot_name"]}', '').strip()

        try:
            search_widget = await SearchWidget.create(
                application=self.application,
                chat=request_context.chat,
                session_id=session_id,
                request_id=request_context.request_id,
                query=query,
                page=page,
            )
        except AioRpcError as e:
            if e.code() == StatusCode.INVALID_ARGUMENT or e.code() == StatusCode.CANCELLED:
                request_context.error_log(e)
                return await event.answer(
                    t('MAINTENANCE_WO_PIC', request_context.chat.language),
                )
            raise e

        request_context.statbox(
            action='documents_retrieved',
            duration=time.time() - start_time,
            query=query,
            page=page,
            scored_documents=len(search_widget.scored_documents),
        )

        serp, buttons = await search_widget.render(message_id=message_id)
        return await asyncio.gather(
            event.answer(),
            message.edit(serp, buttons=buttons, link_preview=False)
        )
