from typing import (
    Optional,
    Set,
)

from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.sharience_pb2 import Sharience as ShariencePb
from pypika import (
    PostgreSQLQuery,
    Table,
)
from pypika.terms import Array

from ..base import BaseAction


class ToPostgresAction(BaseAction):
    sharience_table = Table('sharience')
    db_multi_fields = {
        'ipfs_multihashes',
    }
    db_single_fields = {
        'id',
        'parent_id',
        'uploader_id',
        'filesize',
        'md5',
        'updated_at',
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

    def cast_field_value(self, field_name: str, field_value):
        if field_name in self.db_multi_fields:
            field_value = Array(*field_value)
        return field_name, field_value

    def is_field_set(self, sharience_pb: ShariencePb, field_name: str):
        field_value = getattr(sharience_pb, field_name)
        return field_value

    def generate_insert_sql(self, sharience_pb: ShariencePb, fields: Optional[Set[str]] = None):
        columns = []
        inserts = []

        fields = fields or self.db_fields
        for field_name in fields:
            if self.is_field_set(sharience_pb, field_name):
                field_value = getattr(sharience_pb, field_name)
                field_name, field_value = self.cast_field_value(field_name, field_value)
                columns.append(field_name)
                inserts.append(field_value)

        query = PostgreSQLQuery.into(self.sharience_table).columns(*columns).insert(*inserts)
        return query.returning(self.sharience_table.id).get_sql()

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        update_document_pb = document_operation_pb.update_document
        sharience_pb = update_document_pb.typed_document.sharience
        fields = update_document_pb.fields or self.db_fields

        sql = self.generate_insert_sql(
            sharience_pb=sharience_pb,
            fields=fields,
        )
        result = [row async for row in self.pool_holder.iterate(sql)]
        sharience_pb.id = result[0][0]

        return document_operation_pb
