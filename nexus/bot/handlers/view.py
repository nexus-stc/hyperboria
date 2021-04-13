import asyncio

from library.telegram.base import RequestContext
from nexus.bot.exceptions import MessageHasBeenDeletedError
from nexus.translations import t
from telethon import (
    events,
    functions,
)
from telethon.errors import MessageIdInvalidError

from .base import BaseHandler


class ViewHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/v([ab])([sr])?_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)_'
                                                      '([0-9]+)')
    should_reset_last_widget = False

    def parse_pattern(self, event: events.ChatAction):
        short_schema = event.pattern_match.group(1)
        schema = self.short_schema_to_schema(short_schema)
        session_id = event.pattern_match.group(3)
        old_message_id = int(event.pattern_match.group(4))
        document_id = int(event.pattern_match.group(5))
        position = int(event.pattern_match.group(6))

        page = int(position / self.application.config['application']['page_size'])

        return schema, session_id, old_message_id, document_id, position, page

    async def process_widgeting(self, has_found_old_widget, old_message_id, request_context: RequestContext):
        if has_found_old_widget:
            message_id = old_message_id
            link_preview = None
        else:
            old_message = (await self.application.telegram_client(
                functions.messages.GetMessagesRequest(id=[old_message_id])
            )).messages[0]
            prefetch_message = await self.application.telegram_client.send_message(
                request_context.chat.chat_id,
                t("SEARCHING", language=request_context.chat.language),
                reply_to=old_message.reply_to_msg_id,
            )
            self.application.user_manager.last_widget[request_context.chat.chat_id] = prefetch_message.id
            message_id = prefetch_message.id
            link_preview = True
        return message_id, link_preview

    async def compose_back_command(
        self,
        session_id,
        message_id,
        page,
    ):
        return f'/search_{session_id}_{message_id}_{page}'

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        schema, session_id, old_message_id, document_id, position, page = self.parse_pattern(event)

        request_context.add_default_fields(mode='view', session_id=session_id)
        request_context.statbox(action='view', document_id=document_id, position=position, schema=schema)

        has_found_old_widget = old_message_id == self.application.user_manager.last_widget.get(request_context.chat.chat_id)

        try:
            message_id, link_preview = await self.process_widgeting(
                has_found_old_widget=has_found_old_widget,
                old_message_id=old_message_id,
                request_context=request_context
            )

            document_view = await self.resolve_document(
                schema,
                document_id,
                position,
                session_id,
                request_context,
            )
            try:
                back_command = await self.compose_back_command(
                    session_id=session_id,
                    message_id=message_id,
                    page=page,
                )
            except MessageHasBeenDeletedError:
                return await event.respond(
                    t('REPLY_MESSAGE_HAS_BEEN_DELETED', language=request_context.chat.language),
                )

            view, buttons = document_view.get_view(
                language=request_context.chat.language,
                session_id=session_id,
                bot_external_name=self.application.config['telegram']['bot_external_name'],
                position=position,
                back_command=back_command,
            )
            actions = [
                self.application.telegram_client.edit_message(
                    request_context.chat.chat_id,
                    message_id,
                    view,
                    buttons=buttons,
                    link_preview=link_preview,
                ),
                event.delete(),
            ]
            if not has_found_old_widget:
                actions.append(
                    self.application.telegram_client.delete_messages(
                        request_context.chat.chat_id,
                        [old_message_id],
                    )
                )
            return await asyncio.gather(*actions)
        except MessageIdInvalidError:
            await event.reply(t("VIEWS_CANNOT_BE_SHARED", language=request_context.chat.language))
