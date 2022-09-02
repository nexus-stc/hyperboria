import asyncio
import logging
import time
from typing import Iterable

from aiokafka import AIOKafkaProducer
from izihawa_utils.exceptions import NeedRetryError
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.actions.common import canonize_doi
from nexus.models.proto.operation_pb2 import \
    CrossReferenceOperation as CrossReferenceOperationPb
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.operation_pb2 import UpdateDocument as UpdateDocumentPb
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from nexus.models.proto.typed_document_pb2 import \
    TypedDocument as TypedDocumentPb
from pypika import (
    Parameter,
    PostgreSQLQuery,
    Table,
)
from tenacity import (
    retry,
    retry_if_exception_type,
    wait_fixed,
)

from .base import Processor


class CrossReferencesProcessor(Processor):
    scimag_table = Table('scimag')
    cross_references_table = Table('cross_references')
    topic = 'cross_references'

    def __init__(self, bootstrap_servers, database):
        super().__init__()
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
            max_size=1,
        )
        self.bootstrap_servers = bootstrap_servers
        self.producer = None
        self.starts.append(self.pool_holder)

    async def start(self):
        self.producer = self.get_producer()
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()
            self.producer = None

    def get_producer(self):
        return AIOKafkaProducer(
            loop=asyncio.get_event_loop(),
            bootstrap_servers=self.bootstrap_servers,
        )

    @retry(retry=retry_if_exception_type(NeedRetryError), wait=wait_fixed(15))
    async def process_bulk(self, messages: Iterable[CrossReferenceOperationPb]):
        need_delay = False
        for message in messages:
            if message.retry_count > 1:
                logging.getLogger('error').warning({
                    'status': 'error',
                    'error': 'not_found',
                    'source': message.source,
                    'target': message.target,
                })
                continue

            if time.time() - message.last_retry_unixtime < 60:
                need_delay = True
                await self.producer.send_and_wait(
                    'cross_references',
                    message.SerializeToString(),
                )
                continue
            source = canonize_doi(message.source)
            target = canonize_doi(message.target)
            target_row = [row async for row in self.pool_holder.iterate(
                PostgreSQLQuery
                .from_('scimag')
                .select('id')
                .where(self.scimag_table.doi == Parameter('%s'))
                .get_sql(),
                values=(target,)
            )]

            if not target_row:
                if message.retry_count == 0:
                    document_operation = DocumentOperationPb(
                        update_document=UpdateDocumentPb(
                            full_text_index=True,
                            should_fill_from_external_source=True,
                            typed_document=TypedDocumentPb(scimag=ScimagPb(doi=target)),
                        ),
                    )

                    await self.producer.send_and_wait(
                        'operations_binary',
                        document_operation.SerializeToString(),
                    )
                new_message = CrossReferenceOperationPb()
                new_message.CopyFrom(message)
                new_message.retry_count += 1
                new_message.last_retry_unixtime = int(time.time())
                await self.producer.send_and_wait(
                    self.topic,
                    new_message.SerializeToString(),
                )
                continue

            target_id = target_row[0][0]
            source_subquery = (
                PostgreSQLQuery
                .from_('scimag')
                .select('id')
                .where(self.scimag_table.doi == source)
            )
            await self.pool_holder.execute(
                PostgreSQLQuery
                .into('cross_references')
                .columns(
                    'source_id',
                    'target_id',
                )
                .insert(source_subquery, target_id)
                .on_conflict(self.cross_references_table.source_id, self.cross_references_table.target_id)
                .do_nothing()
                .get_sql()
            )
        if need_delay:
            await asyncio.sleep(1.0)
