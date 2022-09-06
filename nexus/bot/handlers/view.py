import asyncio
import time

from library.telegram.base import RequestContext
from library.telegram.utils import safe_execution
from nexus.translations import t
from nexus.views.telegram.base_holder import BaseHolder
from telethon import (
    events,
    functions,
)
from telethon.errors import MessageIdInvalidError

from .base import BaseHandler


def is_earlier_than_2_days(message):
    return time.time() - time.mktime(message.date.timetuple()) < 2 * 24 * 60 * 60 - 10


class ViewHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/v([ab])([sr])?_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)_([0-9]+)')
    should_reset_last_widget = False

    def parse_pattern(self, event: events.ChatAction):
        short_index_alias = event.pattern_match.group(1)
        index_alias = self.short_index_alias_to_index_alias(short_index_alias)
        session_id = event.pattern_match.group(3)
        old_message_id = int(event.pattern_match.group(4))
        document_id = int(event.pattern_match.group(5))
        position = int(event.pattern_match.group(6))
        page = int(position / self.application.config['application']['page_size'])

        return index_alias, session_id, old_message_id, document_id, position, page

    async def get_message(self, message_id):
        get_message_request = functions.messages.GetMessagesRequest(id=[message_id])
        messages = await self.application.telegram_client(get_message_request)
        return messages.messages[0]

    async def process_widgeting(self, has_found_old_widget, old_message, request_context: RequestContext):
        if has_found_old_widget and is_earlier_than_2_days(old_message):
            message_id = old_message.id
        else:
            prefetch_message = await self.application.telegram_client.send_message(
                request_context.chat.chat_id,
                t("SEARCHING", request_context.chat.language),
                reply_to=old_message.reply_to_msg_id,
            )
            self.application.user_manager.last_widget[request_context.chat.chat_id] = prefetch_message.id
            message_id = prefetch_message.id
        return message_id

    async def compose_back_command(self, session_id, message_id, page):
        return f'/search_{session_id}_{message_id}_{page}'

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        index_alias, session_id, old_message_id, document_id, position, page = self.parse_pattern(event)

        request_context.add_default_fields(mode='view', session_id=session_id)
        request_context.statbox(
            action='view',
            document_id=document_id,
            position=position,
            index_alias=index_alias
        )

        old_message = await self.get_message(old_message_id)
        has_found_old_widget = old_message_id == self.application.user_manager.last_widget.get(request_context.chat.chat_id)
        language = request_context.chat.language

        try:
            message_id = await self.process_widgeting(
                has_found_old_widget=has_found_old_widget,
                old_message=old_message,
                request_context=request_context,
            )
            typed_document_pb = await self.resolve_document(
                index_alias,
                document_id,
                position,
                session_id,
                request_context,
            )
            holder = BaseHolder.create(typed_document_pb=typed_document_pb)
            back_command = await self.compose_back_command(session_id=session_id, message_id=message_id, page=page)

            promo = self.application.promotioner.choose_promotion(language)
            view_builder = holder.view_builder(language).add_view(
                bot_name=self.application.config['telegram']['bot_name']
            ).add_new_line(2).add(promo, escaped=True)
            buttons = holder.buttons_builder(language).add_back_button(back_command).add_default_layout(
                bot_name=self.application.config['telegram']['bot_name'],
                session_id=session_id,
                position=position,
            ).build()
            actions = [
                self.application.telegram_client.edit_message(
                    request_context.chat.chat_id,
                    message_id,
                    view_builder.build(),
                    buttons=buttons,
                    link_preview=view_builder.has_cover,
                ),
                event.delete(),
            ]
            if not has_found_old_widget:
                async with safe_execution(error_log=request_context.error_log):
                    await self.application.telegram_client.delete_messages(request_context.chat.chat_id, [old_message_id])
            return await asyncio.gather(*actions)
        except MessageIdInvalidError:
            await event.reply(t("VIEWS_CANNOT_BE_SHARED", language))
