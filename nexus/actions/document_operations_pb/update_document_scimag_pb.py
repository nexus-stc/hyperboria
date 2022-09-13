import asyncio
import logging
from typing import (
    Optional,
    Set,
)

import orjson as json
from aiocrossref import CrossrefClient
from aiocrossref.exceptions import (
    NotFoundError,
    WrongContentTypeError,
)
from aiokafka import AIOKafkaProducer
from aiosumma import SummaClient
from izihawa_utils.common import filter_none
from izihawa_utils.pb_to_json import MessageToDict
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.actions import scimag_pb
from nexus.actions.base import BaseAction
from nexus.actions.common import canonize_doi
from nexus.actions.crossref_api import ToScimagPbAction
from nexus.actions.exceptions import InterruptProcessing
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
from summa.proto import index_service_pb2 as index_service_pb


class ToPostgresAction(BaseAction):
    scimag_table = Table('scimag')
    db_multi_fields = {
        'authors',
        'ipfs_multihashes',
        'isbns',
        'issns',
        'tags',
    }
    db_single_fields = {
        'id',
        'abstract',
        'container_title',
        'content',
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
        'page_rank',
        'referenced_by_count',
        'scimag_bulk_id',
        'title',
        'type',
        'updated_at',
        'volume',
    }
    db_fields = db_single_fields | db_multi_fields

    def __init__(self, database):
        super().__init__()
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
        )
        self.starts.append(self.pool_holder)

    def cast_field_value(self, field_name: str, field_value):
        if field_name in self.db_multi_fields:
            field_value = Array(*field_value)
        return field_name, field_value

    def is_field_set(self, scimag_pb: ScimagPb, field_name: str):
        field_value = getattr(scimag_pb, field_name)
        if field_name in {'scimag_bulk_id', 'issued_at'}:
            return scimag_pb.HasField(field_name)
        return field_value

    def generate_insert_sql(self, scimag_pb: ScimagPb, fields: Optional[Set[str]] = None):
        columns = []
        params = []

        fields = fields or self.db_fields
        for field_name in fields:
            if self.is_field_set(scimag_pb, field_name):
                field_value = getattr(scimag_pb, field_name)
                field_name, field_value = self.cast_field_value(field_name, field_value)
                columns.append(field_name)
                params.append(field_value)

        query = PostgreSQLQuery.into(self.scimag_table).columns(*columns).insert(*params)
        if columns:
            query = query.on_conflict('doi')
            for field, val in zip(columns, params):
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
            sql = self.generate_update_sql(
                scimag_pb,
                fields=fields,
            )
            await self.pool_holder.execute(sql)
        else:
            sql = self.generate_insert_sql(
                scimag_pb=scimag_pb,
                fields=fields,
            )
            result = [row async for row in self.pool_holder.iterate(sql)]
            scimag_pb.id = result[0][0]
        return document_operation_pb


class ToSummaAction(BaseAction):
    forbidden_types = {
        'book-series',
        'book-set',
        'book-track',
        'component',
        'dataset',
        'journal',
        'journal-issue',
        'journal-volume',
        'peer-review',
        'proceedings',
        'report-series',
    }

    def __init__(self, kafka, summa):
        super().__init__()
        self.kafka = kafka
        self.producer = None
        self.summa_config = summa
        self.summa_client = SummaClient(endpoint=summa['endpoint'])

    async def start(self):
        self.producer = self.get_producer()
        await self.producer.start()
        await self.summa_client.start()

    async def stop(self):
        await self.summa_client.stop()
        if self.producer:
            await self.producer.stop()
            self.producer = None

    def get_producer(self):
        return AIOKafkaProducer(
            loop=asyncio.get_running_loop(),
            bootstrap_servers=self.kafka['bootstrap_servers'],
            max_request_size=self.kafka['max_request_size'],
        )

    async def async_index(self, scimag_pb: ScimagPb):
        for topic_name in self.kafka['topic_names']:
            await self.producer.send_and_wait(
                topic_name,
                index_service_pb.IndexOperation(
                    index_document=index_service_pb.IndexDocumentOperation(
                        document=json.dumps(filter_none(MessageToDict(scimag_pb, preserving_proto_field_name=True))),
                    ),
                ).SerializeToString(),
            )

    async def sync_index(self, scimag_pb: ScimagPb):
        document = filter_none(MessageToDict(scimag_pb, preserving_proto_field_name=True))
        logging.getLogger('statbox').info({'action': 'sync_index', 'document': document})
        await self.summa_client.index_document(index_alias=self.summa_config['index_alias'], document=document)
        await self.summa_client.commit_index(index_alias=self.summa_config['index_alias'])

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scimag_pb = update_document_pb.typed_document.scimag
        if scimag_pb.type in self.forbidden_types:
            return document_operation_pb
        if not scimag_pb.HasField('issued_at'):
            scimag_pb.issued_at = -62135596800
        if update_document_pb.full_text_index:
            if update_document_pb.full_text_index_commit:
                await self.sync_index(scimag_pb=scimag_pb)
            else:
                await self.async_index(scimag_pb=scimag_pb)
        return document_operation_pb


class ReferencesToKafkaAction(BaseAction):
    def __init__(self, kafka):
        super().__init__()
        self.kafka = kafka
        self.producer = None

    async def start(self):
        self.producer = self.get_producer()
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()
            self.producer = None

    def get_producer(self):
        return AIOKafkaProducer(
            loop=asyncio.get_running_loop(),
            bootstrap_servers=self.kafka['bootstrap_servers'],
        )

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scimag_pb = update_document_pb.typed_document.scimag
        for reference in scimag_pb.references:
            reference_operation = CrossReferenceOperationPb(
                source=scimag_pb.doi,
                target=reference,
            )
            for topic_name in self.kafka['topic_names']:
                await self.producer.send_and_wait(
                    topic_name,
                    reference_operation.SerializeToString(),
                )

        return document_operation_pb


class FillFromExternalSourceAction(BaseAction):
    def __init__(self, crossref):
        super().__init__()
        self.crossref_client = CrossrefClient(
            max_retries=crossref.get('max_retries', 15),
            proxy_url=crossref.get('proxy_url'),
            retry_delay=crossref.get('retry_delay', 0.5),
            timeout=crossref.get('timeout'),
            user_agent=crossref.get('user_agent'),
            ttl_dns_cache=crossref.get('ttl_dns_cache'),
        )
        self.doi_client = self.crossref_client
        self.crossref_api_to_scimag_pb_action = ToScimagPbAction()
        self.starts.append(self.crossref_client)

    async def try_resolve(self, doi, look_at_doi_org=False):
        try:
            return await self.crossref_client.works(doi=doi)
        except (WrongContentTypeError, NotFoundError) as e:
            if look_at_doi_org:
                doi_org_response = await self.doi_client.get(doi=doi)
                if doi_org_response:
                    resolved_doi = canonize_doi(doi_org_response.get('published-print', {}).get('DOI'))
                    if resolved_doi:
                        try:
                            return await self.crossref_client.works(doi=resolved_doi)
                        except (WrongContentTypeError, NotFoundError) as e:
                            raise InterruptProcessing(document_id=doi, reason=str(e))
            raise InterruptProcessing(document_id=doi, reason=str(e))

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scimag_pb = update_document_pb.typed_document.scimag
        if not update_document_pb.should_fill_from_external_source:
            return document_operation_pb
        crossref_api_response = await self.try_resolve(doi=scimag_pb.doi)
        new_scimag_pb = await self.crossref_api_to_scimag_pb_action.do(crossref_api_response)
        scimag_pb.MergeFrom(new_scimag_pb)
        return document_operation_pb


class CleanAction(BaseAction):
    def __init__(self):
        super().__init__()
        self.cleaner = scimag_pb.CleanAction()
        self.language_detect = scimag_pb.DetectLanguageAction()
        self.starts.append(self.cleaner)

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scimag_pb = update_document_pb.typed_document.scimag
        scimag_pb = await self.cleaner.do(scimag_pb)
        scimag_pb = await self.language_detect.do(scimag_pb)
        if update_document_pb.fields and (scimag_pb.language or scimag_pb.meta_language):
            fields = set(update_document_pb.fields)
            if scimag_pb.language:
                fields.add('language')
            if scimag_pb.meta_language:
                fields.add('meta_language')
            del update_document_pb.fields[:]
            update_document_pb.fields.extend(fields)
        update_document_pb.typed_document.scimag.CopyFrom(scimag_pb)
        return document_operation_pb
