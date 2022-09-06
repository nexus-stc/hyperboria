import asyncio
import io
import re
import zipfile

from izihawa_nlptools.regex import DOI_REGEX
from library.telegram.base import RequestContext
from library.telegram.common import close_button
from nexus.bot.exceptions import UnknownFileFormatError
from nexus.hub.proto import submitter_service_pb2 as submitter_service_pb
from nexus.translations import t
from telethon import events

from .base import BaseHandler


class SubmitHandler(BaseHandler):
    filter = events.NewMessage(
        func=lambda e: e.document and e.document.mime_type in ('application/pdf', 'application/zip'),
        incoming=True
    )
    is_group_handler = True
    writing_handler = True

    def get_doi_hint(self, message, reply_message):
        doi_hint = None
        if message.raw_text:
            doi_regex = re.search(DOI_REGEX, message.raw_text)
            if doi_regex:
                doi_hint = doi_regex.group(1) + '/' + doi_regex.group(2)
        if not doi_hint and reply_message:
            doi_regex = re.search(DOI_REGEX, reply_message.raw_text)
            if doi_regex:
                doi_hint = doi_regex.group(1) + '/' + doi_regex.group(2)
        return doi_hint

    async def handler(self, event, request_context: RequestContext):
        session_id = self.generate_session_id()

        request_context.add_default_fields(session_id=session_id)
        request_context.statbox(action='show', mode='submit', mime_type=event.document.mime_type)

        reply_to = None
        message = event
        reply_message = await event.get_reply_message()
        if reply_message:
            reply_to = reply_message.id

        doi_hint = self.get_doi_hint(message=message, reply_message=reply_message)
        skip_analysis = '⚡️' in message.raw_text
        user_id = message.sender_id
        request_context.statbox(
            action='analyzed',
            mode='submit',
            doi_hint=doi_hint,
            skip_analysis=skip_analysis,
            reply_to=reply_to,
        )

        match event.document.mime_type:
            case 'application/pdf':
                return await self.application.hub_client.submit(
                    file=submitter_service_pb.TelegramFile(
                        document=bytes(event.document),
                        file_id=event.file.id,
                        message_id=event.id,
                    ),
                    chat=request_context.chat,
                    bot_name=request_context.bot_name,
                    reply_to=reply_to,
                    request_id=request_context.request_id,
                    session_id=session_id,
                    doi_hint=doi_hint,
                    skip_analysis=skip_analysis,
                    uploader_id=user_id,
                )
            case 'application/zip':
                if request_context.is_personal_mode():
                    try:
                        file_data = await self.application.telegram_client.download_document(
                            document=event.document,
                            file=bytes,
                        )
                        request_context.statbox(action='unpack', mode='submit', size=len(file_data))
                        with zipfile.ZipFile(io.BytesIO(file_data), 'r') as zf:
                            for filename in zf.namelist():
                                if not filename.lower().endswith('.pdf'):
                                    continue
                                nested_file = zf.read(filename)
                                request_context.statbox(
                                    action='unpacked_file',
                                    mode='submit',
                                    filename=filename,
                                    size=len(nested_file),
                                )
                                await self.application.hub_client.submit(
                                    file=submitter_service_pb.PlainFile(
                                        data=nested_file,
                                        filename=filename,
                                    ),
                                    chat=request_context.chat,
                                    bot_name=request_context.bot_name,
                                    reply_to=reply_to,
                                    request_id=request_context.request_id,
                                    session_id=session_id,
                                    uploader_id=user_id,
                                )
                    finally:
                        return await event.delete()
            case _:
                request_context.statbox(action='unknown_file_format')
                request_context.error_log(UnknownFileFormatError(format=event.document.mime_type))
                return await asyncio.gather(
                    event.reply(
                        t('UNKNOWN_FILE_FORMAT_ERROR', request_context.chat.language),
                        buttons=None if request_context.is_group_mode() else [close_button()],
                    ),
                    event.delete(),
                )


class EditSubmitHandler(SubmitHandler):
    filter = events.MessageEdited(func=lambda e: e.document, incoming=True)
