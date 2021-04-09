import re
import time

from grpc.experimental.aio import AioRpcError
from library.telegram.base import RequestContext
from nexus.bot.widgets.document_list_widget import DocumentListWidget
from nexus.translations import t
from telethon import events

from .base import BaseCallbackQueryHandler


class ReferencingToHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern=re.compile('^/r_([A-Za-z0-9]+)_([0-9]+)', re.DOTALL))
    should_reset_last_widget = False

    async def do_request(self, request_context: RequestContext, session_id: str, message_id: int, document_id: int, page: int):
        start_time = time.time()
        try:
            document_list_widget = await DocumentListWidget.create(
                application=self.application,
                chat=request_context.chat,
                session_id=session_id,
                message_id=message_id,
                request_id=request_context.request_id,
                referencing_to=document_id,
                page=page,
            )
        except AioRpcError as e:
            raise e

        action = 'referencing_to_found'
        if len(document_list_widget.scored_documents) == 0:
            action = 'referencing_to_not_found'

        request_context.statbox(
            action=action,
            duration=time.time() - start_time,
            query=f'{document_id}',
        )

        serp, buttons = await document_list_widget.render()
        return await self.application.telegram_client.edit_message(
            request_context.chat.id,
            message_id,
            serp,
            buttons=buttons,
            link_preview=False,
        )

    async def handler(self, event, request_context: RequestContext):
        session_id = event.pattern_match.group(1).decode()
        document_id = int(event.pattern_match.group(2).decode())

        request_context.add_default_fields(
            mode='referencing_to',
            session_id=session_id,
        )

        prefetch_message = await event.respond(
            t("SEARCHING", language=request_context.chat.language),
        )
        message_id = prefetch_message.id

        return await self.do_request(
            request_context=request_context,
            session_id=session_id,
            message_id=message_id,
            document_id=document_id,
            page=0,
        )


class ReferencingToPagingHandler(ReferencingToHandler):
    filter = events.CallbackQuery(pattern=re.compile('^/rp_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)_([0-9]+)', re.DOTALL))

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id = event.pattern_match.group(1).decode()
        message_id = int(event.pattern_match.group(2).decode())
        document_id = int(event.pattern_match.group(3).decode())
        page = int(event.pattern_match.group(4).decode())

        request_context.add_default_fields(
            mode='referencing_to_paging',
            session_id=session_id,
        )

        return await self.do_request(
            request_context=request_context,
            session_id=session_id,
            message_id=message_id,
            document_id=document_id,
            page=page,
        )
