import time

from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from nexus.bot.application import TelegramApplication


class BanlistWidget:
    def __init__(self, application: TelegramApplication, chat: ChatPb):
        self.application = application
        self.chat = chat

    async def render(self, chat_list: list[ChatPb]):
        if not chat_list:
            return 'Nobody is banned'
        separator = '------------\n'
        return separator.join(
            map(
                lambda chat: (
                    f'```{chat.username} ({chat.chat_id})\n'
                    f'Until: {time.ctime(chat.ban_until)}\n'
                    f'Message: {chat.ban_message}```\n'
                    f'/unban_{chat.chat_id}\n'
                ),
                chat_list
            )
        )
