from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from pypika import (
    PostgreSQLQuery,
    Table,
)

from ..base import BaseAction


class ToPostgresAction(BaseAction):
    votes_table = Table('votes')

    def __init__(self, database):
        super().__init__()
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
            max_size=1,
        )
        self.starts.append(self.pool_holder)

    def generate_insert_sql(self, document_id: int, value: int, voter_id: int):
        query = PostgreSQLQuery.into(self.votes_table).columns(
            'document_id',
            'value',
            'voter_id',
        ).insert(
            document_id,
            value,
            voter_id,
        )
        query = query.on_conflict('document_id', 'voter_id').do_update('value', value)
        return query.get_sql()

    async def do(self, document_operation_pb: DocumentOperationPb) -> DocumentOperationPb:
        vote_pb = document_operation_pb.vote
        sql = self.generate_insert_sql(
            document_id=vote_pb.document_id,
            value=vote_pb.value,
            voter_id=vote_pb.voter_id,
        )
        await self.pool_holder.execute(sql)
        return vote_pb
