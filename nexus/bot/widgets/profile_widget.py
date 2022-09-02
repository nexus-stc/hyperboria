from typing import Optional

from idm.api.proto import (
    chat_manager_service_pb2,
    profile_service_pb2,
    subscription_manager_service_pb2,
)
from izihawa_nlptools.utils import escape_format
from library.telegram.common import close_button
from nexus.bot.application import TelegramApplication
from nexus.views.telegram.common import (
    TooLongQueryError,
    encode_query_to_deep_link,
)
from telethon import Button


def limits(text, limit, with_dots: bool = False):
    if len(text) > limit:
        text = text[:limit]
        if with_dots:
            text += '...'
    return text


class ProfileWidget:
    def __init__(
        self,
        application: TelegramApplication,
        request_context,
        profile: profile_service_pb2.GetProfileResponse,
    ):
        self.application = application
        self.profile = profile
        self.request_context = request_context

    # ToDo: deduplicate functions
    def encode_link(self, bot_name, text, query):
        try:
            encoded_query = encode_query_to_deep_link(query, bot_name)
            return f'[{text}]({encoded_query})'
        except TooLongQueryError:
            return text

    def get_deep_tag_link(self, bot_name, tag):
        query = f'tags:"{tag}"'
        return self.encode_link(bot_name, tag, query)

    def get_deep_issn_link(self, bot_name, text, issns):
        query = ['order_by:date']
        for issn in issns[:2]:
            query.append(f'issn:{issn}')
        return self.encode_link(bot_name, text=escape_format(text), query=' '.join(query))

    def encode_rating(self):
        if self.profile.uploads_count > 1000:
            return '🏆'
        elif self.profile.uploads_count > 100:
            return '🥇'
        elif self.profile.uploads_count > 10:
            return '🥈'
        elif self.profile.uploads_count > 0:
            return '🥉'
        else:
            return '💩'

    def encode_subscription(self, subscription: subscription_manager_service_pb2.Subscription):
        match subscription.subscription_type:
            case subscription_manager_service_pb2.Subscription.Type.CUSTOM:
                return f'`{subscription.subscription_query}`'
            case subscription_manager_service_pb2.Subscription.Type.DIGEST:
                return f'🥘 Daily digest'
            case subscription_manager_service_pb2.Subscription.Type.DOI:
                return f'🔬 `{subscription.subscription_query}`'
            case _:
                return f'{subscription.subscription_query}'

    async def render(self) -> tuple[str, Optional[list]]:
        profile_view = f'Nexus Rating: {self.encode_rating()}'

        if self.profile.most_popular_tags:
            links = [
                self.get_deep_tag_link(
                    bot_name=self.application.config['telegram']['bot_name'],
                    tag=escape_format(tag)
                ) for tag in self.profile.most_popular_tags
            ]
            profile_view += ('\n\nInterested in: ' + " - ".join(links))

        if self.request_context.is_personal_mode() or self.profile.is_connectome_enabled:
            if self.profile.most_popular_series:
                links = [
                    '- ' + self.get_deep_issn_link(
                        bot_name=self.application.config['telegram']['bot_name'],
                        text=series.name,
                        issns=series.issns,
                    ) for series in self.profile.most_popular_series
                ]
                profile_view += ('\n\nMost read journals:\n' + "\n".join(links))
            if self.profile.downloaded_documents[:5]:
                display_documents = []
                for downloaded_document in self.profile.downloaded_documents[:5]:
                    title = limits(escape_format(downloaded_document.title), limit=100, with_dots=True)
                    link = self.encode_link(
                        bot_name=self.application.config['telegram']['bot_name'],
                        text=title,
                        query=f"id:{downloaded_document.id}"
                    )
                    display_documents.append(f'- {link}')
                profile_view += ('\n\nLast read:\n' + "\n".join(display_documents))

        if self.request_context.is_personal_mode() and self.profile.subscriptions:
            display_subscriptions = []
            for subscription in self.profile.subscriptions[:5]:
                display_subscriptions.append('- ' + self.encode_subscription(subscription))
            profile_view += ('\n\nSubscriptions:\n' + "\n".join(display_subscriptions))
            if len(self.profile.subscriptions) > 5:
                profile_view += f'\n`and {len(self.profile.subscriptions) - 5} more...`'

        if self.request_context.is_personal_mode():
            if self.profile.is_connectome_enabled:
                profile_view += f'\n\nYou can hide your profile from others in /settings'
            else:
                profile_view += f'\n\nYou can make your profile visible in /settings'

        digest_button = Button.inline(
            '✨ Digest',
            data='/digest',
        )

        return profile_view, [digest_button, close_button()] if self.request_context.is_personal_mode() else None
