import logging

from izihawa_utils.pb_to_json import MessageToDict
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb
from pypika import (
    PostgreSQLQuery,
    Table,
    functions,
)
from pypika.terms import Array

from .. import scitech_pb
from ..base import BaseAction
from ..exceptions import ConflictError


class UuidFunction(functions.Function):
    def __init__(self, uuid, name=None):
        super(UuidFunction, self).__init__('UUID', uuid, name=name)


class ToPostgresAction(BaseAction):
    scitech_table = Table('scitech')
    db_single_fields = {
        'id',
        'cu',
        'cu_suf',
        'description',
        'doi',
        'edition',
        'extension',
        'fiction_id',
        'filesize',
        'is_deleted',
        'issued_at',
        'language',
        'libgen_id',
        'meta_language',
        'md5',
        'original_id',
        'pages',
        'series',
        'title',
        'updated_at',
        'volume',
    }
    db_multi_fields = {
        'authors',
        'ipfs_multihashes',
        'isbns',
        'tags',
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
        self.waits.append(self.pool_holder)

    def cast_field_value(self, field_name, field_value):
        if field_name in self.db_multi_fields:
            field_value = Array(*field_value)
        if field_name in {'title', }:
            field_value = field_value.replace('\0', '').strip()
        return field_name, field_value

    def is_field_set(self, scitech_pb: ScitechPb, field_name: str):
        field_value = getattr(scitech_pb, field_name)
        if field_name in {'issued_at', }:
            return scitech_pb.HasField(field_name)
        return field_value

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        scitech_pb = update_document_pb.typed_document.scitech
        fields = update_document_pb.fields or self.db_fields

        conditions = []
        if scitech_pb.id:
            conditions.append(self.scitech_table.id == scitech_pb.id)
        if scitech_pb.libgen_id:
            conditions.append(self.scitech_table.libgen_id == scitech_pb.libgen_id)
        if scitech_pb.fiction_id:
            conditions.append(self.scitech_table.fiction_id == scitech_pb.fiction_id)
        if scitech_pb.doi:
            conditions.append(self.scitech_table.doi == scitech_pb.doi)
        # if scitech_pb.md5:
            # conditions.append(self.scitech_table.md5 == UuidFunction(scitech_pb.md5))

        if conditions:
            casted_conditions = conditions[0]
            for condition in conditions[1:]:
                casted_conditions = casted_conditions | condition
            sql = (
                PostgreSQLQuery
                .from_(self.scitech_table)
                .select(functions.Count('*'))
                .where(casted_conditions)
                .get_sql()
            )
            result = [row async for row in self.pool_holder.iterate(sql)]
            count = result[0][0]

            if count > 1:
                raise ConflictError(scitech_pb, duplicates=[])

            if count == 1:
                query = PostgreSQLQuery.update(self.scitech_table)
                for field_name in fields:
                    if self.is_field_set(scitech_pb, field_name):
                        field_value = getattr(scitech_pb, field_name)
                        field_name, field_value = self.cast_field_value(field_name, field_value)
                        query = query.set(field_name, field_value)
                sql = query.where(casted_conditions).returning('id', 'original_id').get_sql()
            else:
                columns = []
                inserts = []
                for field_name in fields:
                    if self.is_field_set(scitech_pb, field_name):
                        field_value = getattr(scitech_pb, field_name)
                        field_name, field_value = self.cast_field_value(field_name, field_value)
                        columns.append(field_name)
                        inserts.append(field_value)
                query = (
                    PostgreSQLQuery
                    .into(self.scitech_table)
                    .columns(*columns)
                    .insert(*inserts)
                    .on_conflict('libgen_id', 'doi')
                )
                for col, val in zip(columns, inserts):
                    query = query.do_update(col, val)
                sql = query.returning('id', 'original_id').get_sql()

            try:
                result = [row async for row in self.pool_holder.iterate(sql)]
            except:
                logging.getLogger('error').error({'sql': sql, 'scitech': MessageToDict(scitech_pb)})
                raise
            scitech_pb.id, scitech_pb.original_id = result[0][0], result[0][1] or 0
            return document_operation_pb


class CleanAction(BaseAction):
    def __init__(self):
        super().__init__()
        self.cleaner = scitech_pb.CleanAction()
        self.waits.append(self.cleaner)

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        update_document_pb.typed_document.scitech.CopyFrom(await self.cleaner.do(update_document_pb.typed_document.scitech))
        return document_operation_pb
