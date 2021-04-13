import asyncio

from aioipfs import AsyncIPFS
from library.aiogrpctools.base import BaseService
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
    def __init__(self, service_name: str, bot_external_name: str, ipfs_config: dict, telegram_client):
        super().__init__(service_name=service_name)
        self.bot_external_name = bot_external_name
        self.ipfs_client = AsyncIPFS(host=ipfs_config['address'], port=ipfs_config['port'])
        self.telegram_client = telegram_client

    async def get_ipfs_hashes(self, file):
        return list(map(
            lambda x: x['Hash'],
            await asyncio.gather(
                self.ipfs_client.add_bytes(file, cid_version=1, hash='blake2b-256', only_hash=True),
                self.ipfs_client.add_bytes(file, cid_version=0, hash='sha2-256', only_hash=True),
            )
        ))

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((rpcerrorlist.TimeoutError, ValueError)),
    )
    async def send_file(
        self,
        document_view,
        file,
        request_context,
        session_id,
        document_id=None,
        voting=True,
        progress_callback=None,
    ):
        if document_id is None:
            document_id = document_view.id
        buttons = None
        if voting:
            buttons = [
                vote_button(
                    case='broken',
                    schema=document_view.schema,
                    document_id=document_id,
                    language=request_context.chat.language,
                    session_id=session_id,
                ),
                vote_button(
                    case='ok',
                    schema=document_view.schema,
                    document_id=document_id,
                    language=request_context.chat.language,
                    session_id=session_id,
                ),
            ]
        message = await self.telegram_client.send_file(
            attributes=[DocumentAttributeFilename(document_view.get_filename())],
            buttons=buttons,
            caption=f"{document_view.generate_body(language=request_context.chat.language, limit=512)}\n"
                    f"@{self.bot_external_name}",
            entity=request_context.chat.chat_id,
            file=file,
            progress_callback=progress_callback
        )
        request_context.statbox(
            action='sent',
            document_id=document_id,
            schema=document_view.schema,
            voting=voting,
        )
        return message
