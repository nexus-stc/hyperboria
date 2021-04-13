from library.telegram.base import RequestContext
from nexus.hub.proto.delivery_service_pb2 import \
    StartDeliveryResponse as StartDeliveryResponsePb
from nexus.translations import t
from nexus.views.telegram.common import remove_button
from telethon import events

from .base import BaseCallbackQueryHandler


class DownloadHandler(BaseCallbackQueryHandler):
    filter = events.CallbackQuery(pattern='^/dl([abcm])_([A-Za-z0-9]+)_([0-9]+)_([0-9]+)$')
    is_group_handler = True

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        short_schema = event.pattern_match.group(1).decode()
        schema = self.short_schema_to_schema(short_schema)
        session_id = event.pattern_match.group(2).decode()
        document_id = int(event.pattern_match.group(3))
        position = int(event.pattern_match.group(4).decode())

        self.application.user_manager.last_widget[request_context.chat.chat_id] = None

        request_context.add_default_fields(mode='download', session_id=session_id)
        request_context.statbox(action='get', document_id=document_id, position=position, schema=schema)

        typed_document_pb = await self.get_typed_document_pb(
            schema=schema,
            document_id=document_id,
            request_context=request_context,
            session_id=session_id,
            position=position,
        )
        start_delivery_response_pb = await self.application.hub_client.start_delivery(
            typed_document_pb=typed_document_pb,
            chat=request_context.chat,
            request_id=request_context.request_id,
            session_id=session_id,
        )
        if start_delivery_response_pb.status == StartDeliveryResponsePb.Status.ALREADY_DOWNLOADING:
            await event.answer(
                f'{t("ALREADY_DOWNLOADING", language=request_context.chat.language)}',
            )
            await remove_button(event, '⬇️', and_empty_too=True)
        elif start_delivery_response_pb.status == StartDeliveryResponsePb.Status.TOO_MANY_DOWNLOADS:
            await event.answer(
                f'{t("TOO_MANY_DOWNLOADS", language=request_context.chat.language)}',
            )
        else:
            await remove_button(event, '⬇️', and_empty_too=True)
            self.application.user_manager.last_widget[request_context.chat.chat_id] = None
