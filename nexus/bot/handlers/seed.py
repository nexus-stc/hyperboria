import io
import re

from library.telegram.base import RequestContext
from library.telegram.common import close_button
from library.telegram.utils import safe_execution
from nexus.translations import t
from nlptools.izihawa_nlptools.utils import cast_string_to_single_string
from telethon import events
from telethon.tl.types import DocumentAttributeFilename

from .base import BaseHandler


class SeedHandler(BaseHandler):
    filter = events.NewMessage(
        incoming=True,
        pattern=re.compile(r'^/(r)?seed(?:@\w+)?'
                           r'(?:(?:\s+(\d+))?(?:\s+(\d+))?(\n+.*)?)?$'),
    )
    is_group_handler = False

    async def handler(self, event: events.ChatAction, request_context: RequestContext):
        session_id = self.generate_session_id()
        request_context.add_default_fields(mode='seed', session_id=session_id)

        random_seed = True if event.pattern_match.group(1) else False

        if string_offset := event.pattern_match.group(2):
            offset = int(string_offset.strip() or 0)
        else:
            offset = 0

        if string_limit := event.pattern_match.group(3):
            limit = min(int(string_limit.strip()), 10000)
        else:
            limit = offset
            offset = 0

        original_query = ''
        if string_query := event.pattern_match.group(4):
            original_query = string_query.strip()
            query = f'+({original_query}) +ipfs_multihashes:[* TO *]'
        else:
            query = '+ipfs_multihashes:[* TO *]'

        if not string_query and not string_limit and not string_offset:
            request_context.statbox(action='help')
            return await event.reply(t('SEED_HELP', language=request_context.chat.language), buttons=[close_button()])

        wait_message = await event.respond(t('SEED_GENERATION', language=request_context.chat.language))
        async with safe_execution(error_log=request_context.error_log):
            await event.delete()

        request_context.statbox(
            action='request',
            offset=offset,
            limit=limit,
            query=query,
        )

        if random_seed:
            meta_search_response = await self.application.meta_api_client.meta_search(
                index_aliases=['scitech', ],
                query=query,
                collectors=[{
                    'reservoir_sampling': {
                        'limit': limit,
                        'fields': ['ipfs_multihashes', 'doi', 'md5'],
                    }
                }, {
                    'count': {}
                }],
                skip_cache_loading=True,
                skip_cache_saving=True,
                query_tags=['seed'],
            )
            documents = meta_search_response.collector_outputs[0].reservoir_sampling.random_documents
            count = meta_search_response.collector_outputs[1].count.count
        else:
            meta_search_response = await self.application.meta_api_client.meta_search(
                index_aliases=['scitech', ],
                query=query,
                collectors=[{
                    'top_docs': {
                        'limit': limit,
                        'offset': offset,
                        'scorer': {'eval_expr': '-updated_at'},
                        'fields': ['ipfs_multihashes', 'doi', 'md5'],
                    }
                }, {
                    'count': {}
                }],
                query_tags=['seed'],
            )
            documents = meta_search_response.collector_outputs[0].top_docs.scored_documents
            count = meta_search_response.collector_outputs[1].count.count

        buffer = io.BytesIO()
        for document in documents:
            buffer.write(document.document.encode())
            buffer.write(b'\n')
        buffer.flush()

        casted_query = cast_string_to_single_string(original_query)
        if not casted_query:
            casted_query = 'cids'
        filename = f'{casted_query[:16]}-{offset}-{limit}-{count}.cids.txt'
        oneliner = f'cat {filename} | jq -c -r ".ipfs_multihashes[0]" | xargs -I{{}} ipfs pin add {{}}'

        query_head = f'`{original_query}`\n\n' if original_query else ''
        offset_head = f'**Offset:** {offset}\n' if not random_seed else ''
        await self.application.telegram_client.send_file(
            attributes=[DocumentAttributeFilename(filename)],
            buttons=[close_button()],
            caption=f'{query_head}'
                    f'{offset_head}'
                    f'**Limit:** {limit}\n'
                    f'**Total:** {count}\n\n'
                    f'**One-liner:** \n'
                    f'`{oneliner}`',
            entity=request_context.chat.chat_id,
            file=buffer.getvalue(),
            reply_to=event,
        )
        buffer.close()
        async with safe_execution(error_log=request_context.error_log):
            await self.application.telegram_client.delete_messages(request_context.chat.chat_id, [wait_message.id])
