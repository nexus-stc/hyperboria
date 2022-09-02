import logging
import time
from abc import ABC
from datetime import datetime

from grpc import StatusCode
from grpc.experimental.aio import AioRpcError
from idm.api.proto.chat_manager_service_pb2 import Chat as ChatPb
from izihawa_utils.exceptions import BaseError
from izihawa_utils.random import random_string
from library.logging import error_log
from library.telegram.base import RequestContext
from library.telegram.common import close_button
from library.telegram.utils import safe_execution
from nexus.bot.application import TelegramApplication
from nexus.bot.exceptions import UnknownIndexAliasError
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from nexus.translations import t
from telethon import (
    TelegramClient,
    events,
    functions,
)
from telethon.errors import (
    QueryIdInvalidError,
    UserNotParticipantError,
)


def get_username(event: events.ChatAction, chat):
    if event.is_group or event.is_channel:
        return str(event.chat_id)
    else:
        return chat.username


def get_language(event: events.ChatAction, chat):
    if event.is_group or event.is_channel:
        return 'en'
    return chat.lang_code


def is_banned(chat: ChatPb) -> bool:
    return chat.ban_until is not None and datetime.utcnow().timestamp() < chat.ban_until


class ReadOnlyModeError(BaseError):
    level = logging.WARNING
    code = 'read_only_mode_error'


class BaseHandler(ABC):
    # Is handler working in the groups
    is_group_handler = False
    # Is subscription to the `config['telegram']['related_channel'] required to use this handler
    is_subscription_required_for_handler = False
    # Telethon filter
    filter = events.NewMessage(incoming=True)
    should_reset_last_widget = True
    # Raises StopPropagation in the end of handling. It means this handler would be the last one in chain
    stop_propagation = True
    # If set to True then read_only mode will disable handler
    writing_handler = False

    def __init__(self, application: TelegramApplication):
        self.application = application
        self.index_alias_to_resolver = {
            'scimag': self.resolve_scimag,
            'scitech': self.resolve_scitech,
        }
        self.short_index_alias_to_index_alias_dict = {
            'a': 'scimag',
            'b': 'scitech',
        }

    def generate_session_id(self) -> str:
        return random_string(self.application.config['application']['session_id_length'])

    def short_index_alias_to_index_alias(self, short_index_alias: str) -> str:
        return self.short_index_alias_to_index_alias_dict[short_index_alias]

    async def get_last_messages_in_chat(self, event: events.ChatAction):
        messages_holder = await self.application.telegram_client(functions.messages.GetMessagesRequest(
            id=list(range(event.id + 1, event.id + 10)))
        )
        if messages_holder:
            return messages_holder.messages
        return []

    async def get_typed_document_pb(
        self,
        index_alias: str,
        document_id: int,
        mode: str,
        request_context: RequestContext,
        session_id: str,
        position: int,
    ) -> TypedDocumentPb:
        return await self.application.meta_api_client.get(
            index_alias=index_alias,
            document_id=document_id,
            mode=mode,
            session_id=session_id,
            position=position,
            request_id=request_context.request_id,
            user_id=str(request_context.chat.chat_id),
        )

    async def resolve_scimag(
        self,
        document_id: int,
        position: int,
        request_context: RequestContext,
        session_id: str,
    ) -> TypedDocumentPb:
        return await self.get_typed_document_pb(
            index_alias='scimag',
            document_id=document_id,
            mode='view',
            position=position,
            request_context=request_context,
            session_id=session_id,
        )

    async def resolve_scitech(
        self,
        document_id: int,
        position: int,
        request_context: RequestContext,
        session_id: str,
    ) -> TypedDocumentPb:
        return await self.get_typed_document_pb(
            index_alias='scitech',
            document_id=document_id,
            mode='view',
            position=position,
            request_context=request_context,
            session_id=session_id,
        )

    async def resolve_document(
        self,
        index_alias: str,
        document_id: int,
        position: int,
        session_id: str,
        request_context: RequestContext
    ) -> TypedDocumentPb:
        if index_alias not in self.index_alias_to_resolver:
            raise UnknownIndexAliasError(index_alias=index_alias)

        resolver = self.index_alias_to_resolver[index_alias]
        return await resolver(
            document_id=document_id,
            position=position,
            request_context=request_context,
            session_id=session_id,
        )

    def reset_last_widget(self, chat_id: int):
        self.application.user_manager.last_widget[chat_id] = None

    def register_for(self, telegram_client: TelegramClient):
        telegram_client.add_event_handler(self._wrapped_handler, self.filter)
        return self._wrapped_handler

    async def _send_fail_response(self, event: events.ChatAction, request_context: RequestContext):
        try:
            await event.reply(
                t('MAINTENANCE', request_context.chat.language).format(
                    maintenance_picture_url=self.application.config['application']['maintenance_picture_url'],
                ),
                buttons=None if request_context.is_group_mode() else [close_button()]
            )
        except (ConnectionError, QueryIdInvalidError, ValueError) as e:
            request_context.error_log(e)

    async def _put_chat(self, event: events.ChatAction, request_id: str):
        event_chat = await event.get_chat()
        username = get_username(event, event_chat)
        language = get_language(event, event_chat)
        if not self.application.idm_client:
            return ChatPb(
                chat_id=event.chat_id,
                username=username,
                language=language,
            )
        try:
            chat = await self.application.idm_client.get_chat(
                chat_id=event.chat_id,
                request_id=request_id,
            )
            return chat
        except AioRpcError as e:
            if e.code() != StatusCode.NOT_FOUND:
                raise
            if self.application.config['application']['is_read_only_mode']:
                raise ReadOnlyModeError()
            if language not in {'en', 'ru'}:
                language = 'en'
            chat = await self.application.idm_client.create_chat(
                chat_id=event.chat_id,
                username=username,
                language=language,
                request_id=request_id,
            )
            return chat

    async def _check_ban(self, event: events.ChatAction, request_context: RequestContext, chat: ChatPb):
        if is_banned(chat):
            if chat.ban_message is not None:
                async with safe_execution(
                    error_log=request_context.error_log,
                    on_fail=lambda: self._send_fail_response(event, request_context),
                ):
                    await event.reply(t('BANNED', chat.language).format(
                        datetime=str(time.ctime(chat.ban_until)),
                        reason=chat.ban_message,
                    ))
            raise events.StopPropagation()

    async def _check_maintenance(self, event: events.ChatAction):
        if (
            self.application.config['application']['is_maintenance_mode']
            and event.chat_id not in self.application.config['application']['bypass_maintenance']
        ):
            await event.reply(
                t('UPGRADE_MAINTENANCE', 'en').format(
                    upgrade_maintenance_picture_url=self.application.config['application']
                    ['upgrade_maintenance_picture_url']
                ),
                buttons=None if (event.is_group or event.is_channel) else [close_button()]
            )
            raise events.StopPropagation()

    async def _check_read_only(self, event: events.ChatAction):
        if self.application.config['application']['is_read_only_mode']:
            await event.reply(
                t("READ_ONLY_MODE", 'en'),
            )
            raise events.StopPropagation()

    async def is_subscribed(self, chat: ChatPb) -> bool:
        if chat.chat_id < 0 or chat.created_at > time.time() - 10 * 60:
            return True
        try:
            await self.application.telegram_client.get_permissions(
                self.application.config['telegram']['related_channel'],
                chat.chat_id,
            )
        except UserNotParticipantError:
            return False
        return True

    async def _check_subscription(self, event: events.ChatAction, request_context: RequestContext, chat: ChatPb):
        if (
            self.application.config['application']['is_subscription_required']
            and self.is_subscription_required_for_handler
            and not await self.is_subscribed(chat)
        ):
            async with safe_execution(
                error_log=request_context.error_log,
                on_fail=lambda: self._send_fail_response(event, request_context),
            ):
                await event.reply(t(
                    'SUBSCRIBE_TO_CHANNEL',
                    language=chat.language
                ).format(related_channel=self.application.config['telegram']['related_channel']))
            raise events.StopPropagation()

    def _has_access(self, chat: ChatPb) -> bool:
        return True

    async def _process_chat(self, event: events.ChatAction, request_id: str):
        try:
            chat = await self._put_chat(event, request_id=request_id)
        except (AioRpcError, BaseError) as e:
            error_log(e)
            event_chat = await event.get_chat()
            username = get_username(event, event_chat)
            chat = ChatPb(
                chat_id=event.chat_id,
                is_system_messaging_enabled=True,
                is_discovery_enabled=True,
                is_connectome_enabled=False,
                language='en',
                username=username,
                is_admin=False,
            )
        return chat

    async def _wrapped_handler(self, event: events.ChatAction) -> None:
        # Checking group permissions
        if (event.is_group or event.is_channel) and not self.is_group_handler:
            return

        await self._check_maintenance(event=event)
        await self._check_read_only(event=event)

        request_id = RequestContext.generate_request_id(self.application.config['application']['request_id_length'])
        chat = await self._process_chat(event=event, request_id=request_id)

        request_context = RequestContext(
            bot_name=self.application.config['telegram']['bot_name'],
            chat=chat,
            request_id=request_id,
            request_id_length=self.application.config['application']['request_id_length'],
        )

        if not self._has_access(chat):
            return

        await self._check_subscription(event=event, request_context=request_context, chat=chat)
        await self._check_ban(event=event, request_context=request_context, chat=chat)

        if self.should_reset_last_widget:
            self.reset_last_widget(request_context.chat.chat_id)

        async with safe_execution(
            error_log=request_context.error_log,
            on_fail=lambda: self._send_fail_response(event, request_context),
        ):
            await self.handler(
                event,
                request_context=request_context,
            )
        if self.stop_propagation:
            raise events.StopPropagation()

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        raise NotImplementedError()


class BaseCallbackQueryHandler(BaseHandler, ABC):
    async def _send_fail_response(self, event, request_context: RequestContext):
        try:
            await event.answer(t('MAINTENANCE_WO_PIC', request_context.chat.language))
        except (ConnectionError, QueryIdInvalidError) as e:
            request_context.error_log(e)
