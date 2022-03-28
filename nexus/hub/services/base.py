import asyncio

from aioipfs import AsyncIPFS as AsyncIPFS
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
    def __init__(self, service_name: str, ipfs_config: dict, telegram_clients):
        super().__init__(service_name=service_name)
        self.ipfs_client = None
        self.ipfs_config = ipfs_config
        self.telegram_clients = telegram_clients

    async def start(self):
        self.ipfs_client = AsyncIPFS(host=self.ipfs_config['address'], port=self.ipfs_config['port'])

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
                    index_alias=document_view.index_alias,
                    document_id=document_id,
                    language=request_context.chat.language,
                    session_id=session_id,
                ),
                vote_button(
                    case='ok',
                    index_alias=document_view.index_alias,
                    document_id=document_id,
                    language=request_context.chat.language,
                    session_id=session_id,
                ),
            ]

        caption = (
            f"{document_view.generate_body(language=request_context.chat.language, limit=512)}\n"
            f"@{request_context.bot_name}"
        )
        message = await self.telegram_clients[request_context.bot_name].send_file(
            attributes=[DocumentAttributeFilename(document_view.get_filename())],
            buttons=buttons,
            caption=caption,
            entity=request_context.chat.chat_id,
            file=file,
            progress_callback=progress_callback
        )
        request_context.statbox(
            action='sent',
            document_id=document_id,
            index_alias=document_view.index_alias,
            voting=voting,
        )
        return message
