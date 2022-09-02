import asyncio

from library.aiogrpctools.base import BaseService
from library.telegram.common import close_button
from nexus.views.telegram.common import vote_button
from telethon.errors import rpcerrorlist
from telethon.tl.types import DocumentAttributeFilename
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
)


def is_group_or_channel(chat_id: int):
    return chat_id < 0


class BaseHubService(BaseService):
    async def item_found(self, bot_name, doi):
        if mutual_aid_service := self.application.mutual_aid_services.get(bot_name):
            await mutual_aid_service.delete_request(doi)
        await self.application.idm_client.reschedule_subscriptions(
            subscriptions_ids=dict(
                subscription_query=f'doi:{doi}',
            ),
            new_schedule={'schedule': '*/1 * * * *'},
        )

    async def get_ipfs_hashes(self, file):
        return list(map(
            lambda x: x['Hash'],
            await asyncio.gather(
                self.application.ipfs_client.add_bytes(file, cid_version=1, hash='blake2b-256', only_hash=True),
                self.application.ipfs_client.add_bytes(file, cid_version=0, hash='sha2-256', only_hash=True),
            )
        ))

    def set_fields_from_processed(self, document_pb, processed_document):
        new_fields = []
        if processed_document.get('abstract') and not document_pb.abstract:
            document_pb.abstract = processed_document['abstract']
            new_fields.append('abstract')
        if processed_document.get('body') and not document_pb.content:
            document_pb.content = processed_document['body']
            new_fields.append('content')
        return new_fields

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((rpcerrorlist.TimeoutError, ValueError)),
    )
    async def send_file(
        self,
        document_holder,
        file,
        request_context,
        session_id,
        document_id=None,
        voting=True,
        close=False,
        progress_callback=None,
        chat_id=None,
        reply_to=None,
    ):
        if document_id is None:
            document_id = document_holder.id
        buttons = []
        if voting:
            buttons += [
                vote_button(
                    case='broken',
                    index_alias=document_holder.index_alias,
                    document_id=document_id,
                    language=request_context.chat.language,
                    session_id=session_id,
                ),
                vote_button(
                    case='ok',
                    index_alias=document_holder.index_alias,
                    document_id=document_id,
                    language=request_context.chat.language,
                    session_id=session_id,
                ),
            ]
        if close:
            buttons += [
                close_button(session_id=session_id)
            ]
        if not buttons:
            buttons = None
        short_description = (
            document_holder.view_builder(request_context.chat.language)
            .add_short_description().add_doi_link(label=True, on_newline=True).build()
        )
        caption = (
            f"{short_description}\n"
            f"@{self.application.config['telegram']['related_channel']}"
        )
        message = await self.application.telegram_clients[request_context.bot_name].send_file(
            attributes=[DocumentAttributeFilename(document_holder.get_filename())],
            buttons=buttons,
            caption=caption,
            entity=chat_id or request_context.chat.chat_id,
            file=file,
            progress_callback=progress_callback,
            reply_to=reply_to,
        )
        request_context.statbox(
            action='sent',
            voting=voting,
        )
        return message
