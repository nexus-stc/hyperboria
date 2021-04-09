import asyncio
import logging
import re
import time

from grpc import StatusCode
from grpc.experimental.aio import AioRpcError
from library.telegram.base import RequestContext
from nexus.bot.widgets.search_widget import SearchWidget
from nexus.translations import t
from nexus.views.telegram.common import close_button
from nexus.views.telegram.registry import parse_typed_document_to_view
from telethon import (
    events,
    functions,
)

from .base import (
    BaseCallbackQueryHandler,
    BaseHandler,
)


class BaseSearchHandler(BaseHandler):
    should_reset_last_widget = False

    async def do_search(
        self,
        event: events.ChatAction,
        request_context: RequestContext,
        prefetch_message,
        query: str,
        is_group_mode: bool = False,
        is_shortpath_enabled: bool = False,
    ):
        session_id = self.generate_session_id()
        message_id = prefetch_message.id

        request_context.add_default_fields(is_group_mode=is_group_mode, mode='search', session_id=session_id)

        start_time = time.time()
        try:
            search_widget = await SearchWidget.create(
                application=self.application,
                chat=request_context.chat,
                session_id=session_id,
                message_id=message_id,
                request_id=request_context.request_id,
                query=query,
                is_group_mode=is_group_mode,
            )
        except AioRpcError as e:
            actions = [
                self.application.telegram_client.delete_messages(
                    request_context.chat.id,
                    [message_id],
                )
            ]
            if e.code() == StatusCode.INVALID_ARGUMENT:
                too_difficult_picture_url = self.application.config['application'].get('too_difficult_picture_url', '')
                if e.details() == 'url_query_error':
                    actions.append(
                        event.reply(
                            t('INVALID_QUERY_ERROR', language=request_context.chat.language).format(
                                too_difficult_picture_url=too_difficult_picture_url,
                            ),
                            buttons=[close_button()],
                        )
                    )
                elif e.details() == 'invalid_query_error':
                    actions.append(
                        event.reply(
                            t('INVALID_SYNTAX_ERROR', language=request_context.chat.language).format(
                                too_difficult_picture_url=too_difficult_picture_url,
                            ),
                            buttons=[close_button()],
                        )
                    )
                return await asyncio.gather(*actions)
            elif e.code() == StatusCode.CANCELLED:
                maintenance_picture_url = self.application.config['application'].get('maintenance_picture_url', '')
                request_context.error_log(e)
                actions.append(event.reply(
                    t('MAINTENANCE', language=request_context.chat.language).format(
                        maintenance_picture_url=maintenance_picture_url,
                    ),
                    buttons=[close_button()],
                ))
                return await asyncio.gather(*actions)
            raise e

        action = 'documents_found'
        if len(search_widget.scored_documents) == 0:
            action = 'documents_not_found'

        request_context.statbox(
            action=action,
            duration=time.time() - start_time,
            query=f'page:0 query:{query}',
        )

        if len(search_widget.scored_documents) == 1 and is_shortpath_enabled:
            scored_document = search_widget.scored_documents[0]
            document_view = parse_typed_document_to_view(scored_document.typed_document)
            # Second (re-)fetching is required to retrieve duplicates
            document_view = await self.resolve_document(
                schema=scored_document.typed_document.WhichOneof('document'),
                document_id=document_view.id,
                position=0,
                session_id=session_id,
                request_context=request_context,
            )
            view, buttons = document_view.get_view(
                language=request_context.chat.language,
                session_id=session_id,
                bot_external_name=self.application.config['telegram']['bot_external_name'],
                with_buttons=not is_group_mode,
            )
            return await asyncio.gather(
                self.application.telegram_client.edit_message(
                    request_context.chat.id,
                    message_id,
                    view,
                    buttons=buttons,
                ),
            )

        serp, buttons = await search_widget.render()
        return await self.application.telegram_client.edit_message(
            request_context.chat.id,
            message_id,
            serp,
            buttons=buttons,
            link_preview=False,
        )


class SearchHandler(BaseSearchHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile('^(/search\\s+)?(.*)', flags=re.DOTALL))
    is_group_handler = True
    should_reset_last_widget = False
    is_subscription_required_for_handler = True

    async def ban_handler(self, event: events.ChatAction, request_context: RequestContext, ban_timeout: float):
        logging.getLogger('statbox').info({
            'bot_name': self.application.config['telegram']['bot_name'],
            'action': 'user_flood_ban',
            'mode': 'search',
            'ban_timeout_seconds': ban_timeout,
            'chat_id': request_context.chat.id,
        })
        ban_reason = t(
            'BAN_MESSAGE_TOO_MANY_REQUESTS',
            language=request_context.chat.language
        )
        return await event.reply(t(
            'BANNED_FOR_SECONDS',
            language=request_context.chat.language
        ).format(
            seconds=str(ban_timeout),
            reason=ban_reason,
        ))

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        ban_timeout = self.application.user_manager.check_search_ban_timeout(user_id=request_context.chat.id)
        if ban_timeout:
            return await self.ban_handler(event, request_context, ban_timeout)
        self.application.user_manager.add_search_time(user_id=request_context.chat.id, search_time=time.time())

        search_prefix = event.pattern_match.group(1)
        query = event.pattern_match.group(2)
        is_group_mode = event.is_group or event.is_channel

        if is_group_mode and not search_prefix:
            return
        if not is_group_mode and search_prefix:
            query = event.raw_text
        prefetch_message = await event.reply(
            t("SEARCHING", language=request_context.chat.language),
        )
        self.application.user_manager.last_widget[request_context.chat.id] = prefetch_message.id
        try:
            await self.do_search(
                event, request_context, prefetch_message,
                query=query,
                is_group_mode=is_group_mode,
                is_shortpath_enabled=True,
            )
        except (AioRpcError, asyncio.CancelledError) as e:
            await asyncio.gather(
                event.delete(),
                prefetch_message.delete(),
            )
            raise e


class SearchEditHandler(BaseSearchHandler):
    filter = events.MessageEdited(incoming=True, pattern=re.compile('^(/search\\s+)?(.*)', flags=re.DOTALL))
    is_group_handler = True
    should_reset_last_widget = False

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.add_default_fields(mode='search_edit')
        search_prefix = event.pattern_match.group(1)
        query = event.pattern_match.group(2)
        is_group_mode = event.is_group or event.is_channel
        if is_group_mode and not search_prefix:
            return
        if not is_group_mode and search_prefix:
            query = event.raw_text
        result = await self.application.telegram_client(functions.messages.GetMessagesRequest(
            id=list(range(event.id + 1, event.id + 10)))
        )
        if not result:
            request_context.statbox(action='failed')
            return await event.reply(
                t('REPLY_MESSAGE_HAS_BEEN_DELETED', language=request_context.chat.language),
            )
        for next_message in result.messages:
            if next_message.is_reply and event.id == next_message.reply_to_msg_id:
                request_context.statbox(action='resolved')
                await self.do_search(
                    event,
                    request_context,
                    prefetch_message=next_message,
                    query=query,
                    is_group_mode=is_group_mode,
                )
                return
        request_context.statbox(action='failed')
        return await event.reply(
            t('REPLY_MESSAGE_HAS_BEEN_DELETED', language=request_context.chat.language),
        )


class SearchPagingHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern='^/search_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)$')
    should_reset_last_widget = False

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id = event.pattern_match.group(1).decode()
        message_id = int(event.pattern_match.group(2).decode())
        page = int(event.pattern_match.group(3).decode())

        request_context.add_default_fields(mode='search_paging', session_id=session_id)

        message = await event.get_message()
        if not message:
            return await event.answer()
        reply_message = await message.get_reply_message()
        if not reply_message:
            return await event.respond(
                t('REPLY_MESSAGE_HAS_BEEN_DELETED', language=request_context.chat.language),
            )

        start_time = time.time()
        query = reply_message.raw_text
        try:
            search_widget = await SearchWidget.create(
                application=self.application,
                chat=request_context.chat,
                session_id=session_id,
                message_id=message_id,
                request_id=request_context.request_id,
                query=query,
                page=page,
            )
        except AioRpcError as e:
            if e.code() == StatusCode.INVALID_ARGUMENT or e.code() == StatusCode.CANCELLED:
                request_context.error_log(e)
                return await event.answer(
                    t('MAINTENANCE_WO_PIC', language=request_context.chat.language),
                )
            raise e

        action = 'documents_found'
        if len(search_widget.scored_documents) == 0:
            action = 'documents_not_found'

        request_context.statbox(
            action=action,
            duration=time.time() - start_time,
            query=f'page:{page} query:{query}',
        )
        serp, buttons = await search_widget.render()
        return await asyncio.gather(
            event.answer(),
            message.edit(serp, buttons=buttons, link_preview=False)
        )
