from abc import ABC

from library.telegram.base import RequestContext
from nexus.bot.widgets.admin_widget import AdminWidget
from telethon import events

from .base import BaseHandler


class BaseAdminHandler(BaseHandler, ABC):
    def _has_access(self, chat):
        return chat.is_admin


class AdminHandler(BaseAdminHandler):
    filter = events.NewMessage(incoming=True, pattern='^/admin$')

    async def handler(self, event, request_context: RequestContext):
        request_context.statbox(action='show', mode='admin')
        admin_widget_view = AdminWidget(application=self.application, chat=request_context.chat)
        text = await admin_widget_view.render()
        await event.reply(text)
