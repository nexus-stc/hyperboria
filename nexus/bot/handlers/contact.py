import re

from library.telegram.base import RequestContext
from nexus.bot.configs import config
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class ContactHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern=re.compile('^/contact\\s?(.*)', re.DOTALL))
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        query = event.pattern_match.group(1)
        if query:
            request_context.statbox(action='show', mode='contact', query=query)
            await event.reply(
                t('THANK_YOU_FOR_CONTACT', language=request_context.chat.language).format(
                    related_channel=self.application.config['telegram']['related_channel'],
                ),
            )
        else:
            request_context.statbox(action='show', mode='contact')
            await event.reply(
                t('CONTACT', language=request_context.chat.language).format(
                    btc_donate_address=config['application']['btc_donate_address'],
                    libera_pay_url=config['application']['libera_pay_url'],
                    related_channel=config['telegram']['related_channel'],
                ),
                link_preview=False,
            )
