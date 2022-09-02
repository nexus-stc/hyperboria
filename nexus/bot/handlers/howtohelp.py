from library.telegram.base import RequestContext
from nexus.bot.configs import config
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class HowToHelpHandler(BaseHandler):
    filter = events.NewMessage(incoming=True, pattern='^/howtohelp(@[A-Za-z0-9_]+)?$')
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        request_context.statbox(action='show', mode='howtohelp')
        await event.reply(
            t('HOW_TO_HELP', request_context.chat.language).format(
                amazon_gift_card_recipient=config['application'].get('amazon_gift_card_recipient', '🚫'),
                amazon_gift_card_url=config['application'].get('amazon_gift_card_url', '🚫'),
                btc_donate_address=config['application'].get('btc_donate_address', '🚫'),
                eth_donate_address=config['application'].get('eth_donate_address', '🚫'),
                related_channel=config['telegram'].get('related_channel', '🚫'),
                sol_donate_address=config['application'].get('sol_donate_address', '🚫'),
                xmr_donate_address=config['application'].get('xmr_donate_address', '🚫'),
                xrp_donate_address=config['application'].get('xrp_donate_address', '🚫'),
                xrp_donate_tag=config['application'].get('xrp_donate_tag', '🚫'),
            ))
