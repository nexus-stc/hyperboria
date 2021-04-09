import asyncio
from typing import (
    Optional,
    Set,
)

import aiopg
from aiocrossref import CrossrefClient
from aiocrossref.exceptions import (
    NotFoundError,
    WrongContentTypeError,
)
from aiokafka import AIOKafkaProducer
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.models.proto.operation_pb2 import \
    CrossReferenceOperation as CrossReferenceOperationPb
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb
from pypika import (
    PostgreSQLQuery,
    Table,
)
from pypika.terms import Array

from .base import BaseAction
from .crossref_api import CrossrefApiToScimagPbAction
from .exceptions import InterruptProcessing
from .scimag import CleanScimagPbAction


class SendDocumentOperationUpdateDocumentScimagPbToGoldenPostgresAction(BaseAction):
    scimag_table = Table('scimag')
    db_multi_fields = {
        'authors',
        'ipfs_multihashes',
        'issns',
        'tags',
    }
    db_single_fields = {
        'id',
        'abstract',
        'container_title',
        'doi',
        'embedding',
        'filesize',
        'first_page',
        'is_deleted',
        'issued_at',
        'issue',
        'journal_id',
        'language',
        'last_page',
        'meta_language',
        'md5',
        'ref_by_count',
        'scimag_bulk_id',
        'telegram_file_id',
        'title',
        'type',
        'updated_at',
        'volume',
    }
    db_fields = db_single_fields | db_multi_fields

    def __init__(self, database):
        super().__init__()
        self.pool_holder = AioPostgresPoolHolder(
            fn=aiopg.create_pool,
            dsn=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
            timeout=30,
            pool_recycle=60,
            maxsize=4,
        )
        self.waits.append(self.pool_holder)

    def cast_field_value(self, field_name: str, field_value):
        if field_name in self.db_multi_fields:
            field_value = Array(*field_value)
        return field_name, field_value

    def is_field_set(self, scimag_pb: ScimagPb, field_name: str):
        field_value = getattr(scimag_pb, field_name)
        if field_name in {'scimag_bulk_id', 'issued_at'}:
            return scimag_pb.HasField(field_name)
        return field_value

    def generate_delete_sql(self, scimag_pb: ScimagPb):
        return (
            PostgreSQLQuery
            .from_('scimag')
            .where(self.scimag_table.id == scimag_pb.id)
            .delete()
            .get_sql()
        )

    def generate_insert_sql(self, scimag_pb: ScimagPb, fields: Optional[Set[str]] = None):
        columns = []
        inserts = []

        fields = fields or self.db_fields
        for field_name in fields:
            if self.is_field_set(scimag_pb, field_name):
                field_value = getattr(scimag_pb, field_name)
                field_name, field_value = self.cast_field_value(field_name, field_value)
                columns.append(field_name)
                inserts.append(field_value)

        query = PostgreSQLQuery.into(self.scimag_table).columns(*columns).insert(*inserts)
        if columns:
            query = query.on_conflict('doi')
            for field, val in zip(columns, inserts):
                query = query.do_update(field, val)

        return query.returning(self.scimag_table.id).get_sql()

    def generate_update_sql(
        self,
        scimag_pb: ScimagPb,
        fields: Optional[Set[str]] = None,
    ) -> str:
        query = (
            PostgreSQLQuery
            .update(self.scimag_table)
        )
        fields = fields or self.db_fields
        for field_name in fields:
            if self.is_field_set(scimag_pb, field_name):
                field_value = getattr(scimag_pb, field_name)
                field_name, field_value = self.cast_field_value(field_name, field_value)
                query = query.set(field_name, field_value)
        return query.where(self.scimag_table.id == scimag_pb.id).get_sql()

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scimag_pb = update_document_pb.typed_document.scimag
        fields = update_document_pb.fields or self.db_fields

        if scimag_pb.id:
            if not scimag_pb.is_deleted:
                sql = self.generate_update_sql(
                    scimag_pb,
                    fields=fields,
                )
            else:
                sql = self.generate_delete_sql(scimag_pb)
            await self.pool_holder.execute(sql)
        else:
            sql = self.generate_insert_sql(
                scimag_pb=scimag_pb,
                fields=fields,
            )
            result = await self.pool_holder.execute(sql, fetch=True)
            scimag_pb.id = result[0][0]
        return document_operation_pb


class SendDocumentOperationUpdateDocumentScimagPbReferencesToKafkaAction(BaseAction):
    def __init__(self, topic, brokers):
        super().__init__()
        self.topic = topic
        self.brokers = brokers
        self.producer = None

    async def start(self):
        self.producer = self.get_producer()
        await self.producer.start()

    async def stop(self):
        await self.producer.stop()
        self.producer = None

    def get_producer(self):
        return AIOKafkaProducer(
            loop=asyncio.get_running_loop(),
            bootstrap_servers=self.brokers,
        )

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scimag_pb = update_document_pb.typed_document.scimag
        for reference in scimag_pb.references:
            reference_operation = CrossReferenceOperationPb(
                source=scimag_pb.doi,
                target=reference,
            )
            await self.producer.send_and_wait(
                self.topic,
                reference_operation.SerializeToString(),
            )
        return document_operation_pb


class FillDocumentOperationUpdateDocumentScimagPbFromExternalSourceAction(BaseAction):
    def __init__(self, crossref):
        super().__init__()
        self.crossref_client = CrossrefClient(
            delay=1.0 / crossref['rps'],
            max_retries=crossref.get('max_retries', 15),
            proxy_url=crossref.get('proxy_url'),
            retry_delay=crossref.get('retry_delay', 0.5),
            timeout=crossref.get('timeout'),
            user_agent=crossref.get('user_agent'),
        )
        self.crossref_api_to_scimag_pb_action = CrossrefApiToScimagPbAction()
        self.waits.append(self.crossref_client)

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        if not update_document_pb.should_fill_from_external_source:
            return document_operation_pb
        scimag_pb = update_document_pb.typed_document.scimag
        try:
            crossref_api_response = await self.crossref_client.works(doi=scimag_pb.doi)
        except (WrongContentTypeError, NotFoundError) as e:
            raise InterruptProcessing(doc_id=scimag_pb.doi, reason=str(e))
        new_scimag_pb = await self.crossref_api_to_scimag_pb_action.do(crossref_api_response)
        scimag_pb.MergeFrom(new_scimag_pb)
        return document_operation_pb


class CleanDocumentOperationUpdateDocumentScimagPbAction(BaseAction):
    def __init__(self):
        super().__init__()
        self.cleaner = CleanScimagPbAction()
        self.waits.append(self.cleaner)

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        update_document_pb.typed_document.scimag.CopyFrom(await self.cleaner.do(update_document_pb.typed_document.scimag))
        return document_operation_pb
