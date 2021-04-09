from typing import Optional

from idm.api2.proto.chats_service_pb2 import ChatData as Chat
from idm.api2.proto.location_pb2 import Location
from izihawa_utils.podolsky_encoding import encode
from nexus.bot.application import TelegramApplication
from nexus.translations import t
from telethon import Button

top_languages = {
    'am': '🇪🇹',
    'ar': '🇦🇪',
    'de': '🇩🇪',
    'en': '🇬🇧',
    'es': '🇪🇸',
    'fa': '🇮🇷',
    'hi': '🇮🇳',
    'id': '🇮🇩',
    'it': '🇮🇹',
    'ja': '🇯🇵',
    'ms': '🇲🇾',
    'pb': '🇧🇷',
    'ru': '🇷🇺',
    'tg': '🇹🇯',
    'uk': '🇺🇦',
    'uz': '🇺🇿',
}

boolean_emoji = {
    False: '❎',
    True: '✅️',
}


class SettingsRouterWidget:
    def __init__(self, application: TelegramApplication, chat: Chat, request_id: str = None):
        self.application = application
        self.chat = chat
        self.request_id = request_id

    async def render(self):
        sa = f'🌎{encode("1")}{t("SETUP_AUTOMATICALLY", language=self.chat.language)}'
        sm = f'👇{encode("1")}{t("SETUP_MANUALLY", language=self.chat.language)}'
        return t("SETTINGS_ROUTER_HELP", language=self.chat.language), [[
            Button.text(sa, resize=True, single_use=True),
            Button.text(sm, resize=True, single_use=True),
            Button.force_reply(),
        ]]


class SettingsManualWidget:
    def __init__(
        self,
        application: TelegramApplication,
        chat: Chat,
        has_language_buttons: Optional[bool] = None,
        is_group_mode: bool = False,
        request_id: Optional[str] = None,
    ):
        self.application = application
        self.chat = chat
        self.has_language_buttons = has_language_buttons
        if self.has_language_buttons is None:
            self.has_language_buttons = self.application.config['application']['views']['settings']['has_language_buttons']
        self.is_group_mode = is_group_mode
        self.request_id = request_id
        self._actions = {
            'sl': self._switch_language,
            'ssm': self._switch_system_messaging,
            'sd': self._switch_discovery,
        }

    async def _switch_language(self, target_language: str):
        return await self.application.idm_client.update_chat(
            chat_id=self.chat.id,
            language=target_language,
            request_id=self.request_id,
        )

    async def _switch_system_messaging(self, is_system_messaging_enabled: str):
        self.chat = await self.application.idm_client.update_chat(
            chat_id=self.chat.id,
            is_system_messaging_enabled=bool(int(is_system_messaging_enabled)),
            request_id=self.request_id,
        )
        return self.chat

    async def _switch_discovery(self, is_discovery_enabled: str):
        self.chat = await self.application.idm_client.update_chat(
            chat_id=self.chat.id,
            is_discovery_enabled=bool(int(is_discovery_enabled)),
            request_id=self.request_id,
        )
        return self.chat

    async def set_last_location(self, lon: float, lat: float):
        self.chat = await self.application.idm_client.update_chat(
            chat_id=self.chat.id,
            last_location=Location(lon=lon, lat=lat),
            request_id=self.request_id,
        )
        return

    async def process_action(self, action_id: str, data: str):
        old_chat = self.chat
        await self._actions[action_id](data)
        return old_chat != self.chat

    async def render(self):
        text = t('SETTINGS_TEMPLATE', language=self.chat.language).format(
            bot_version=self.application.config['application']['bot_version'],
            nexus_version=self.application.config['application']['nexus_version'],
            language=top_languages.get(self.chat.language, self.chat.language),
            tzinfo=self.chat.tzinfo or 'UTC',
        )
        if not self.is_group_mode and self.application.config['application']['views']['settings']['has_discovery_button']:
            text = f"{text}\n\n{t('NEXUS_DISCOVERY_DESCRIPTION', language=self.chat.language)}"
        buttons = []
        if self.has_language_buttons:
            buttons.append([])
            for language in sorted(top_languages):
                if len(buttons[-1]) >= 4:
                    buttons.append([])
                buttons[-1].append(
                    Button.inline(
                        text=top_languages[language],
                        data=f'/settings_sl_{language}'
                    )
                )

        if self.is_group_mode:
            return text, buttons

        if self.application.config['application']['views']['settings']['has_system_messaging_button']:
            buttons.append([
                Button.inline(
                    text=(
                        f'{t("SYSTEM_MESSAGING_OPTION", language=self.chat.language)}: '
                        f'{boolean_emoji[self.chat.is_system_messaging_enabled]}'
                    ),
                    data=f'/settings_ssm_{1 - int(self.chat.is_system_messaging_enabled)}'
                )
            ])
        if self.application.config['application']['views']['settings']['has_discovery_button']:
            buttons.append([
                Button.inline(
                    text=(
                        f'{t("DISCOVERY_OPTION", language=self.chat.language)}: '
                        f'{boolean_emoji[self.chat.is_discovery_enabled]}'
                    ),
                    data=f'/settings_sd_{1 - int(self.chat.is_discovery_enabled)}'
                )
            ])
        if self.application.config['application']['views']['settings']['has_location_button']:
            buttons.append([
                Button.request_location('Setup preferences automatically', resize=True)
            ])
        return text, buttons
