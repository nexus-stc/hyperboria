from typing import (
    Any,
    AsyncIterable,
    Iterable,
)

import yaml
from aiosumma import SummaClient
from izihawa_utils.random import generate_request_id
from library.aiopostgres.pool_holder import AioPostgresPoolHolder
from nexus.ingest.jobs.base import BaseJob
from nexus.ingest.sinks.kafka import KafkaSink
from psycopg.rows import dict_row
from summa.proto.utils_pb2 import Desc


class PostgresJob(BaseJob):
    name = 'postgres-job'

    def __init__(
        self,
        batch_size: int,
        database: dict,
        sql: str,
        summa: dict,
        actions: Iterable[dict],
    ):
        kafka_sink = KafkaSink(kafka=summa['kafka'], topic_name=summa['name'])
        super().__init__(actions=actions, sinks=[kafka_sink])
        self.batch_size = batch_size
        self.sql = sql
        self.pool_holder = AioPostgresPoolHolder(
            conninfo=f'dbname={database["database"]} '
            f'user={database["username"]} '
            f'password={database["password"]} '
            f'host={database["host"]}',
            timeout=3600 * 2,
        )
        self.summa_client = SummaClient(endpoint=summa['endpoint'])
        self.summa_config = summa
        self.starts.extend([self.pool_holder, self.summa_client])

    async def init_tables(self, session_id):
        schema = yaml.dump(self.summa_config['index_config']['schema'], default_flow_style=False)
        try:
            await self.summa_client.delete_index(self.summa_config['name'], cascade=True)
        except Exception:
            pass
        await self.summa_client.create_index(
            self.summa_config['name'],
            schema=schema,
            compression='Zstd',
            primary_key=self.summa_config['index_config']['primary_key'],
            default_fields=self.summa_config['index_config']['default_fields'],
            multi_fields=self.summa_config['index_config']['multi_fields'],
            stop_words=self.summa_config['index_config']['stop_words'],
            writer_heap_size_bytes=512 * 1024 * 1024,
            writer_threads=1,
            autocommit_interval_ms=1800 * 1000,
            session_id=session_id,
            sort_by_field=('issued_at', Desc)
        )
        await self.summa_client.create_consumer(
            index_alias=self.summa_config['name'],
            consumer_name=f"{self.summa_config['name']}_consumer",
            topics=[self.summa_config['name']],
            bootstrap_servers=self.summa_config['kafka']['bootstrap_servers'],
            group_id='summa',
            session_id=session_id,
            threads=1,
        )

    async def iterator(self) -> AsyncIterable[Any]:
        session_id = generate_request_id()
        await self.init_tables(session_id)
        if self.batch_size:
            loaded = True
            current = 0
            while loaded:
                loaded = False
                sql = self.sql.format(left=current, right=current + self.batch_size)
                async for row in self.pool_holder.iterate(
                    sql,
                    row_factory=dict_row,
                    # Mandatory for server side cursor
                    cursor_name='nexus_ingest_cursor',
                    itersize=50_000,
                    statement_timeout=3600 * 2,
                ):
                    loaded = True
                    yield row
                current += self.batch_size
        else:
            async for row in self.pool_holder.iterate(
                self.sql,
                row_factory=dict_row,
                # Mandatory for server side cursor
                cursor_name='nexus_ingest_cursor',
                itersize=50_000,
                statement_timeout=3600 * 2,
            ):
                yield row

        await self.summa_client.commit_index(
            self.summa_config['name'],
            session_id=session_id,
        )
        await self.summa_client.set_index_alias(self.summa_config['index_alias'], self.summa_config['name'], session_id=session_id)
