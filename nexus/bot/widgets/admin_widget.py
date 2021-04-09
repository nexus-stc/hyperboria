from idm.api2.proto.chats_service_pb2 import ChatData as Chat
from nexus.bot.application import TelegramApplication


class AdminWidget:
    def __init__(self, application: TelegramApplication, chat: Chat):
        self.application = application
        self.chat = chat

    async def render(self):
        return (
            'Ban: `/ban 12345 20d Spam`\n'
            'Ban (silent): `/ban 12345 100h`\n'
            'List of banned chats: `/banlist`\n'
            'Unban chat: `/unban 12345`'
        )
