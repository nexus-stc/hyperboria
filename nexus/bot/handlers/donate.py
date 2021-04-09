from library.telegram.base import RequestContext
from nexus.bot.configs import config
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class DonateHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/donate(@[A-Za-z0-9_]+)?$')
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.statbox(action='show', mode='donate')
        await event.reply(
            t(
                'DONATE',
                language=request_context.chat.language
            ).format(
                amazon_gift_card_recipient=config['application'].get('amazon_gift_card_recipient', '🚫'),
                amazon_gift_card_url=config['application'].get('amazon_gift_card_url', '🚫'),
                btc_donate_address=config['application'].get('btc_donate_address', '🚫'),
                libera_pay_url=config['application'].get('libera_pay_url', '🚫'),
                related_channel=config['telegram'].get('related_channel', '🚫'),
            ))
