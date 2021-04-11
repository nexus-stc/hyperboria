from library.telegram.base import RequestContext
from nexus.bot.widgets.settings_widget import SettingsWidget
from telethon import events

from .base import (
    BaseCallbackQueryHandler,
    BaseHandler,
)


class SettingsHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/settings(@[A-Za-z0-9_]+)?$')
    is_group_handler = True
    writing_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.add_default_fields(mode='settings_router')
        request_context.statbox(action='show')
        settings_widget = SettingsWidget(
            application=self.application,
            chat=request_context.chat,
            is_group_mode=event.is_group or event.is_channel,
            request_id=request_context.request_id,
        )
        text, buttons = await settings_widget.render()
        await event.reply(text, buttons=buttons)


class SettingsButtonsHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern='^/settings_([A-Za-z0-9]+)_([A-Za-z0-9]+)$')
    is_group_handler = True

    async def handler(self, event, request_context: RequestContext):
        request_context.add_default_fields(mode='settings')
        action_id = event.pattern_match.group(1).decode()
        data = event.pattern_match.group(2).decode()

        request_context.statbox(action='change', query=f'action_id: {action_id} data: {data}')

        settings_widget = SettingsWidget(
            application=self.application,
            chat=request_context.chat,
            is_group_mode=event.is_group or event.is_channel,
            request_id=request_context.request_id,
        )
        is_changed = await settings_widget.process_action(action_id=action_id, data=data)
        text, buttons = await settings_widget.render()
        if not is_changed and not (event.is_group or event.is_channel):
            await event.answer()
            return
        if event.is_group or event.is_channel:
            buttons = None
        await event.edit(text, buttons=buttons)
