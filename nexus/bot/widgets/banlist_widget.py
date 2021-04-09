import time

from idm.api2.proto.chats_service_pb2 import ChatData as Chat
from nexus.bot.application import TelegramApplication


class BanlistWidget:
    def __init__(self, application: TelegramApplication, chat: Chat):
        self.application = application
        self.chat = chat

    async def render(self, chat_list: list[Chat]):
        if not chat_list:
            return 'Nobody is banned'
        separator = '------------\n'
        return separator.join(
            map(
                lambda chat: (
                    f'```{chat.username} ({chat.id})\n'
                    f'Until: {time.ctime(chat.ban_until)}\n'
                    f'Message: {chat.ban_message}```\n'
                    f'/unban_{chat.id}\n'
                ),
                chat_list
            )
        )
