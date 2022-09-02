import asyncio
from collections import defaultdict

from idm.api.proto import (
    profile_service_pb2,
    profile_service_pb2_grpc,
    subscription_manager_service_pb2,
    subscription_manager_service_pb2_grpc,
)
from library.aiogrpctools.base import (
    BaseService,
    aiogrpc_request_wrapper,
)
from psycopg.rows import dict_row
from pypika import (
    CustomFunction,
    PostgreSQLQuery,
    Table,
    functions,
)
from pypika.pseudocolumns import PseudoColumn


class ProfileService(profile_service_pb2_grpc.ProfileServicer, BaseService):
    chats_table = Table('chats')
    scimag_table = Table('scimag')
    scitech_table = Table('scitech')
    sharience_table = Table('sharience')
    subscriptions_table = Table('subscriptions')
    Unnest = CustomFunction('UNNEST', ['column'])

    async def start(self):
        profile_service_pb2_grpc.add_ProfileServicer_to_server(self, self.application.server)

    async def get_downloaded_documents(self, chat_id, starting_from=0, last_n_documents=None):
        if last_n_documents is None:
            last_n_documents = 2**32 - 1

        query = f''' 
            select document_id from telegram_statbox_log 
            where mode = 'download' and action = 'get' 
            and chat_id = {chat_id} and event_datetime > FROM_UNIXTIME({starting_from})
            order by event_datetime desc limit {last_n_documents}
        '''

        document_ids = []
        async for row in self.application.clickhouse_client.iterate(query):
            document_ids.append(row['document_id'])

        if not document_ids:
            return []

        document_query = (
            PostgreSQLQuery
            .from_(self.scimag_table)
            .select(
                self.scimag_table.id,
                self.scimag_table.title,
                self.scimag_table.issns,
                self.scimag_table.tags,
            )
            .where(self.scimag_table.id.isin(document_ids))
            * PostgreSQLQuery
            .from_(self.scitech_table)
            .select(
                self.scitech_table.id,
                self.scitech_table.title,
                PseudoColumn('array[]::text[]').as_('issns'),
                self.scitech_table.tags,
            )
            .where(self.scitech_table.id.isin(document_ids))
        ).get_sql()

        documents_dict = {}
        async for document_row in self.application.pool_holder['nexus'].iterate(document_query, row_factory=dict_row):
            documents_dict[document_row['id']] = profile_service_pb2.ShortDocumentDescription(
                id=document_row['id'],
                title=document_row['title'],
                issns=document_row['issns'],
                tags=document_row['tags'],
            )
        documents = []
        for document_id in document_ids:
            document = documents_dict.get(document_id)
            if document:
                documents.append(document)
        return documents

    async def get_chat_config(self, chat_id):
        async for row in self.application.pool_holder['idm'].iterate(
            PostgreSQLQuery
                .from_(self.chats_table)
                .select(self.chats_table.is_connectome_enabled)
                .where(self.chats_table.chat_id == chat_id)
                .get_sql()
        ):
            return row[0]

    async def get_stats(self, downloaded_documents):
        issns_counter = defaultdict(int)
        tags_counter = defaultdict(int)
        for download_document in downloaded_documents:
            for issn in download_document.issns:
                issns_counter[issn] += 1
            for tag in download_document.tags:
                tags_counter[tag] += 1

        most_popular_issns = sorted(issns_counter, key=issns_counter.get, reverse=True)[:7]
        most_popular_tags = sorted(tags_counter, key=tags_counter.get, reverse=True)[:7]

        most_popular_series = []
        async for row in self.application.pool_holder['nexus'].iterate(
            f"select name, issns from series where issns && array[{most_popular_issns}]::text[]".format(
                most_popular_issns=','.join(map(lambda x: "'" + x + "'", most_popular_issns)),
            ),
            row_factory=dict_row,
        ):
            most_popular_series.append(profile_service_pb2.Series(
                name=row['name'],
                issns=row['issns'],
            ))

        return most_popular_series, most_popular_tags

    async def get_uploads_count(self, chat_id):
        sql = (
            PostgreSQLQuery.from_(self.sharience_table)
            .select(functions.Count(self.sharience_table.parent_id).distinct())
            .groupby(self.sharience_table.uploader_id)
            .where(self.sharience_table.uploader_id == chat_id)
        ).get_sql()
        async for row in self.application.pool_holder['nexus'].iterate(sql):
            return row[0]

    async def get_subscriptions(self, chat_id):
        subscriptions_sql = (
            PostgreSQLQuery.select(
                self.subscriptions_table.id,
                self.subscriptions_table.chat_id,
                self.subscriptions_table.subscription_query,
                self.subscriptions_table.schedule,
                self.subscriptions_table.is_oneshot,
                self.subscriptions_table.is_downloadable,
                self.subscriptions_table.valid_until,
                self.subscriptions_table.next_check_at,
                self.subscriptions_table.subscription_type,
            )
            .from_(self.subscriptions_table)
            .where(self.subscriptions_table.chat_id == chat_id)
            .orderby(self.subscriptions_table.id)
        ).get_sql()
        subscriptions = []
        async for row in self.application.pool_holder['idm'].iterate(subscriptions_sql, row_factory=dict_row):
            subscriptions.append(subscription_manager_service_pb2.Subscription(
                id=row['id'],
                chat_id=row['chat_id'],
                subscription_query=row['subscription_query'],
                schedule=row['schedule'],
                is_oneshot=row['is_oneshot'],
                is_downloadable=row['is_downloadable'],
                valid_until=row['valid_until'],
                next_check_at=row['next_check_at'],
                subscription_type=row['subscription_type'],
            ))
        return subscriptions

    @aiogrpc_request_wrapper()
    async def get_profile(
        self,
        request: profile_service_pb2.GetProfileRequest,
        context,
        metadata,
    ) -> profile_service_pb2.GetProfileResponse:
        downloaded_documents = await self.get_downloaded_documents(
            chat_id=request.chat_id,
            starting_from=request.starting_from,
            last_n_documents=request.last_n_documents if request.HasField('last_n_documents') else None,
        )
        uploads_count, stats, subscriptions, is_connectome_enabled = await asyncio.gather(
            self.get_uploads_count(chat_id=request.chat_id),
            self.get_stats(downloaded_documents=downloaded_documents),
            self.get_subscriptions(chat_id=request.chat_id),
            self.get_chat_config(chat_id=request.chat_id),
        )
        most_popular_series, most_popular_tags = stats
        self.statbox(
            mode='profile',
            action='show',
            chat_id=request.chat_id,
            uploads_count=uploads_count,
            downloads_count=len(downloaded_documents),
            most_popular_tags=most_popular_tags,
            most_popular_series=[series.name for series in most_popular_series],
            is_connectome_enabled=is_connectome_enabled,
        )
        return profile_service_pb2.GetProfileResponse(
            most_popular_tags=most_popular_tags,
            most_popular_series=most_popular_series,
            subscriptions=subscriptions,
            uploads_count=uploads_count,
            downloads_count=len(downloaded_documents),
            downloaded_documents=downloaded_documents if is_connectome_enabled else [],
            is_connectome_enabled=is_connectome_enabled,
        )
