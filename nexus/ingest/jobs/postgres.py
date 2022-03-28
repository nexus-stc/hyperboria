from typing import (
    Any,
    AsyncIterable,
    Iterable,
)

import yaml
from grpc import StatusCode
from grpc.aio import AioRpcError
from izihawa_utils.random import generate_request_id
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.ingest.jobs.base import BaseJob
from nexus.ingest.sinks.kafka import KafkaSink
from psycopg.rows import dict_row
from summa.aiosumma.client import SummaClient


class PostgresJob(BaseJob):
    name = 'postgres-job'

    def __init__(
        self,
        database: dict,
        sql: str,
        summa: dict,
        actions: Iterable[dict],
    ):
        kafka_sink = KafkaSink(kafka_hosts=summa['kafka_hosts'], topic_name=summa['name'])
        super().__init__(actions=actions, sinks=[kafka_sink])
        self.sql = sql
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
        )
        self.summa_client = SummaClient(endpoint=summa['endpoint'])
        self.summa_config = summa
        self.waits.extend([self.pool_holder, self.summa_client])

    async def init_tables(self, session_id):
        try:
            await self.summa_client.delete_index(self.summa_config['name'], session_id=session_id, cascade=True)
        except AioRpcError as e:
            if e.code() != StatusCode.NOT_FOUND:
                raise
        schema = yaml.dump(self.summa_config['index_config']['schema'], default_flow_style=False)
        await self.summa_client.create_index(
            self.summa_config['name'],
            schema=schema,
            primary_key=self.summa_config['index_config']['key_field'],
            default_fields=self.summa_config['index_config']['default_fields'],
            writer_heap_size_bytes=1073741824,
            writer_threads=4,
            autocommit_interval_ms=1800 * 1000,
            session_id=session_id,
        )
        await self.summa_client.create_consumer(
            f"{self.summa_config['name']}_consumer",
            index_name=self.summa_config['name'],
            topics=[self.summa_config['name']],
            bootstrap_servers=self.summa_config['kafka_hosts'],
            group_id='summa',
            session_id=session_id,
            threads=4,
        )

    async def iterator(self) -> AsyncIterable[Any]:
        session_id = generate_request_id()
        await self.init_tables(session_id)
        async for row in self.pool_holder.iterate(
            self.sql,
            row_factory=dict_row,
            # Mandatory for server side cursor
            cursor_name='nexus_ingest_cursor',
            itersize=10_000,
        ):
            yield row
        await self.summa_client.commit_index(self.summa_config['name'], session_id=session_id)
        await self.summa_client.set_index_alias(self.summa_config['alias'], self.summa_config['name'], session_id=session_id)
