from datetime import (
    datetime,
    timedelta,
)

from grpc import StatusCode
from grpc.aio import AioRpcError
from library.telegram.base import RequestContext
from nexus.bot.widgets.banlist_widget import BanlistWidget
from pytimeparse.timeparse import timeparse
from telethon import events

from .admin import BaseAdminHandler


class BanHandler(BaseAdminHandler):
    filter = events.NewMessage(incoming=True, pattern='^/ban (-?[0-9]+) ([A-Za-z0-9]+)\\s?(.*)?$')

    def parse_pattern(self, event: events.ChatAction):
        chat_id = int(event.pattern_match.group(1))
        ban_duration = event.pattern_match.group(2)
        ban_message = event.pattern_match.group(3)
        ban_end_date = datetime.utcnow() + timedelta(seconds=timeparse(ban_duration))

        return chat_id, ban_duration, ban_message, ban_end_date

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        chat_id, ban_duration, ban_message, ban_end_date = self.parse_pattern(event)

        try:
            await self.application.idm_client.update_chat(
                chat_id=chat_id,
                ban_until=int(ban_end_date.timestamp()),
                ban_message=ban_message,
                request_id=request_context.request_id,
            )
            request_context.statbox(
                action='banned',
                ban_message=ban_message,
                ban_until=ban_end_date.timestamp(),
                banned_chat_id=chat_id,
            )
        except AioRpcError as e:
            if e.code() == StatusCode.NOT_FOUND:
                return await event.reply('Chat not found')
            else:
                raise
        return await event.reply('User banned until ' + ban_end_date.strftime("%Y-%m-%d %H:%M") + ' UTC')


class UnbanHandler(BaseAdminHandler):
    filter = events.NewMessage(incoming=True, pattern='^/unban(?:_|\\s)(-?[0-9]+)$')

    async def handler(self, event, request_context: RequestContext):
        chat_id = int(event.pattern_match.group(1))

        try:
            await self.application.idm_client.update_chat(
                chat_id=chat_id,
                ban_until=0,
                request_id=request_context.request_id,
            )
            request_context.statbox(
                action='unbanned',
                unbanned_chat_id=chat_id,
            )
        except AioRpcError as e:
            if e.code() == StatusCode.NOT_FOUND:
                return await event.reply('Chat not found')
            else:
                raise

        return await event.reply('User unbanned')


class BanlistHandler(BaseAdminHandler):
    filter = events.NewMessage(incoming=True, pattern='^/banlist$')

    async def handler(self, event, request_context: RequestContext):
        request_context.statbox(action='show', mode='banlist')
        chat_list = (await self.application.idm_client.list_chats(
            banned_at_moment=int(datetime.utcnow().timestamp()),
            request_id=request_context.request_id,
        )).chats
        banlist_widget_view = BanlistWidget(application=self.application, chat=request_context.chat)
        widget_content = await banlist_widget_view.render(chat_list=chat_list)
        await event.reply(widget_content)
