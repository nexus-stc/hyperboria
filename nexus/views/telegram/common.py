import base64
import binascii
import logging

from izihawa_utils.exceptions import BaseError
from nexus.translations import t
from telethon import Button


class TooLongQueryError(BaseError):
    level = logging.WARNING
    code = 'too_long_query_error'


class DecodeDeepQueryError(BaseError):
    level = logging.WARNING
    code = 'decode_deep_query_error'


def vote_button(language: str, session_id: str, index_alias: str, document_id: int, case: str):
    label = f"REPORT_{case.upper()}_FILE"
    case = {'broken': 'b', 'ok': 'o'}[case]
    short_index_alias = {'scimag': 'a', 'scitech': 'b'}[index_alias]
    return Button.inline(
        text=t(label, language),
        data=f'/vote{short_index_alias}_{session_id}_{document_id}_{case}',
    )


def encode_query_to_deep_link(query, bot_name):
    encoded_query = encode_deep_query(query)
    if len(encoded_query) <= 64:
        return f'https://t.me/{bot_name}?start={encoded_query}'
    raise TooLongQueryError()


def encode_deep_query(query):
    return base64.b64encode(query.encode(), altchars=b'-_').decode()


def decode_deep_query(query):
    try:
        # Padding fix
        return base64.b64decode(query + "=" * ((4 - len(query) % 4) % 4), altchars=b'-_').decode()
    except (binascii.Error, ValueError, UnicodeDecodeError) as e:
        raise DecodeDeepQueryError(nested_error=e)


async def remove_button(event, mark, and_empty_too=False):
    original_message = await event.get_message()
    if original_message:
        original_buttons = original_message.buttons
        buttons = []
        for original_line in original_buttons:
            line = []
            for original_button in original_line:
                if mark in original_button.text or (and_empty_too and not original_button.text.strip()):
                    continue
                line.append(original_button)
            if line:
                buttons.append(line)
        await event.edit(original_message.text, buttons=buttons)
