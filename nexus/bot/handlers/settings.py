from izihawa_utils.podolsky_encoding import encode
from library.telegram.base import RequestContext
from nexus.bot.widgets.settings_widget import (
    SettingsManualWidget,
    SettingsRouterWidget,
)
from nexus.translations import t
from telethon import (
    Button,
    events,
    functions,
)

from .base import (
    BaseCallbackQueryHandler,
    BaseHandler,
)


class SettingsRouterHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/settings(@[A-Za-z0-9_]+)?$')
    is_group_handler = True
    writing_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.add_default_fields(mode='settings_router')
        request_context.statbox(action='show')
        if self.application.config['application']['views']['settings']['has_router']:
            settings_router_widget = SettingsRouterWidget(
                application=self.application,
                chat=request_context.chat,
                request_id=request_context.request_id,
            )
            text, buttons = await settings_router_widget.render()
        else:
            settings_widget = SettingsManualWidget(
                application=self.application,
                chat=request_context.chat,
                is_group_mode=event.is_group or event.is_channel,
                request_id=request_context.request_id,
            )
            text, buttons = await settings_widget.render()
        await event.reply(text, buttons=buttons)


class SettingsAutomaticHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=f'^🌎{encode("1")}')

    async def handler(self, event, request_context: RequestContext):
        request_context.add_default_fields(mode='settings_automatic')
        request_context.statbox(action='show')
        await event.reply(
            f'{t("SEND_YOUR_LOCATION", language=request_context.chat.language)}{encode("sg")}',
            buttons=Button.clear()
        )


class SettingsManualHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=f'^👇{encode("1")}')

    async def handler(self, event, request_context: RequestContext):
        request_context.add_default_fields(mode='settings_manual')
        request_context.statbox(action='show')
        settings_widget = SettingsManualWidget(
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

        settings_manual_widget = SettingsManualWidget(
            application=self.application,
            chat=request_context.chat,
            is_group_mode=event.is_group or event.is_channel,
            request_id=request_context.request_id,
        )
        is_changed = await settings_manual_widget.process_action(action_id=action_id, data=data)
        text, buttons = await settings_manual_widget.render()
        if not is_changed and not (event.is_group or event.is_channel):
            await event.answer()
            return
        if event.is_group or event.is_channel:
            buttons = None
        await event.edit(text, buttons=buttons)


class GeoHandler(BaseHandler):
    filter = events.NewMessage(incoming=True)
    stop_propagation = False

    async def handler(self, event, request_context: RequestContext):
        request_context.add_default_fields(mode='geo')

        if not event.geo:
            return
        request_context.statbox(action='geo', query=f'lon:{event.geo.long} lat:{event.geo.lat}')

        result = await self.application.telegram_client(functions.messages.GetMessagesRequest(id=[event.id - 1]))
        if not result.messages:
            return

        previous_message = result.messages[0]
        if previous_message.message.endswith(encode("sg")):
            request_context.statbox(action='catched_settings')
            settings_manual_widget = SettingsManualWidget(
                application=self.application,
                chat=request_context.chat,
                has_language_buttons=False,
                is_group_mode=event.is_group or event.is_channel,
                request_id=request_context.request_id,
            )
            await settings_manual_widget.set_last_location(lon=event.geo.long, lat=event.geo.lat)
            text, buttons = await settings_manual_widget.render()
            await event.reply(text, buttons=buttons or Button.clear())
            raise events.StopPropagation()
