import logging
import time

from croniter import croniter
from grpc import StatusCode
from idm.api.proto import (
    subscription_manager_service_pb2,
    subscription_manager_service_pb2_grpc,
)
from library.aiogrpctools.base import (
    BaseService,
    aiogrpc_request_wrapper,
)
from psycopg.rows import dict_row
from pypika import (
    PostgreSQLQuery,
    Table,
)


class SubscriptionManagerService(subscription_manager_service_pb2_grpc.SubscriptionManagerServicer, BaseService):
    chats_table = Table('chats')
    subscriptions_table = Table('subscriptions')

    async def start(self):
        subscription_manager_service_pb2_grpc.add_SubscriptionManagerServicer_to_server(self, self.application.server)

    @aiogrpc_request_wrapper(log=False)
    async def get_single_chat_task(
        self,
        request: subscription_manager_service_pb2.SubscribeRequest,
        context,
        metadata,
    ) -> subscription_manager_service_pb2.GetSingleChatTaskRequest:
        subquery = (
            PostgreSQLQuery
            .from_(self.subscriptions_table)
            .select(
                self.subscriptions_table.chat_id,
                self.subscriptions_table.next_check_at,
            )
            .inner_join(self.chats_table)
            .using('chat_id')
            .where(self.chats_table.is_discovery_enabled == True)
            .where(self.subscriptions_table.next_check_at.notnull())
            .where(self.subscriptions_table.valid_until > int(time.time()))
            .orderby(self.subscriptions_table.next_check_at).limit(1)
        )
        query = (
            PostgreSQLQuery.select(
                self.subscriptions_table.id,
                self.subscriptions_table.chat_id,
                self.subscriptions_table.subscription_query,
                self.subscriptions_table.schedule,
                self.subscriptions_table.is_oneshot,
                self.subscriptions_table.is_downloadable,
                self.subscriptions_table.next_check_at,
                self.subscriptions_table.valid_until,
                self.subscriptions_table.subscription_type,
            )
            .from_(self.subscriptions_table)
            .inner_join(subquery)
            .using('chat_id')
            .where(self.subscriptions_table.next_check_at < subquery.next_check_at + 5)
            .orderby(self.subscriptions_table.next_check_at)
        ).get_sql()
        subscriptions = []
        chat_id = None
        async for row in self.application.pool_holder['idm'].iterate(query, row_factory=dict_row):
            chat_id = row['chat_id']
            subscriptions.append(subscription_manager_service_pb2.Subscription(**row))
        return subscription_manager_service_pb2.GetSingleChatTaskResponse(
            subscriptions=subscriptions,
            chat_id=chat_id,
        )

    @aiogrpc_request_wrapper(log=False)
    async def subscribe(
        self,
        request: subscription_manager_service_pb2.SubscribeRequest,
        context,
        metadata,
    ) -> subscription_manager_service_pb2.SubscribeResponse:
        next_check_at = None
        valid_until = request.valid_until if request.HasField('valid_until') else 2 ** 31 - 1
        if request.schedule:
            if not croniter.is_valid(request.schedule):
                return await context.abort(StatusCode.INVALID_ARGUMENT, request.schedule)
            next_check_at = croniter(request.schedule).next(ret_type=float)
        query = (
            PostgreSQLQuery
            .into(self.subscriptions_table)
            .columns(
                self.subscriptions_table.chat_id,
                self.subscriptions_table.subscription_query,
                self.subscriptions_table.schedule,
                self.subscriptions_table.is_oneshot,
                self.subscriptions_table.is_downloadable,
                self.subscriptions_table.valid_until,
                self.subscriptions_table.next_check_at,
                self.subscriptions_table.subscription_type,
            )
            .insert(
                request.chat_id,
                request.subscription_query,
                request.schedule,
                request.is_oneshot,
                request.is_downloadable,
                valid_until,
                next_check_at,
                request.subscription_type
            )
            .on_conflict(
                self.subscriptions_table.chat_id,
                self.subscriptions_table.subscription_query,
            )
            .do_update(
                self.subscriptions_table.valid_until,
                valid_until,
            )
        ).get_sql()
        await self.application.pool_holder['idm'].execute(query)
        return subscription_manager_service_pb2.SubscribeResponse()

    @aiogrpc_request_wrapper(log=False)
    async def reschedule_subscriptions(
        self,
        request: subscription_manager_service_pb2.RescheduleSubscriptionsRequest,
        context,
        metadata,
    ) -> subscription_manager_service_pb2.RescheduleSubscriptionsResponse:
        response_pb = subscription_manager_service_pb2.RescheduleSubscriptionsResponse()
        match str(request.WhichOneof('subscriptions_ids')):
            case 'subscription_id':
                select_condition = self.subscriptions_table.id == request.subscription_id
            case 'subscription_query':
                select_condition = self.subscriptions_table.subscription_query == request.subscription_query
            case _:
                raise RuntimeError(f"Unknown file type {request.WhichOneof('subscriptions_ids')}")

        if request.HasField('new_schedule'):
            schedule = request.new_schedule.schedule
            next_check_at = None
            if request.new_schedule.schedule:
                if not croniter.is_valid(schedule):
                    return await context.abort(StatusCode.INVALID_ARGUMENT, schedule)
                next_check_at = int(croniter(schedule).next(ret_type=float))
            update_sql = (
                PostgreSQLQuery.update(self.subscriptions_table)
                .where(select_condition)
                .set(self.subscriptions_table.next_check_at, next_check_at)
            )
            if request.new_schedule.is_persistent:
                update_sql = update_sql.set(self.subscriptions_table.schedule, schedule)
            update_sql = update_sql.get_sql()
            await self.application.pool_holder['idm'].execute(update_sql)
            logging.getLogger('statbox').info({
                'action': 'rescheduled',
                'mode': 'reschedule_subscriptions',
                'sql': update_sql,
            })
        else:
            select_sql = (
                PostgreSQLQuery
                .from_(self.subscriptions_table).select(
                    self.subscriptions_table.id,
                    self.subscriptions_table.schedule,
                    self.subscriptions_table.is_oneshot)
                .where(select_condition)
            )
            async for row in self.application.pool_holder['idm'].iterate(select_sql.get_sql(), row_factory=dict_row):
                if row['is_oneshot'] and request.is_fired:
                    delete_sql = (
                        PostgreSQLQuery
                        .from_(self.subscriptions_table)
                        .delete()
                        .where(self.subscriptions_table.id == row['id'])
                    ).get_sql()
                    await self.application.pool_holder['idm'].execute(delete_sql)
                    logging.getLogger('statbox').info({
                        'action': 'delete',
                        'mode': 'reschedule_subscriptions',
                        'subscription_id': row['id'],
                        'is_oneshot': row['is_oneshot'],
                        'is_fired': request.is_fired,
                    })
                else:
                    next_check_at = int(croniter(row['schedule']).next(ret_type=float))
                    update_sql = (
                        PostgreSQLQuery
                        .update(self.subscriptions_table)
                        .where(self.subscriptions_table.id == row['id'])
                        .set(self.subscriptions_table.next_check_at, next_check_at)
                    ).get_sql()
                    await self.application.pool_holder['idm'].execute(update_sql)
                    logging.getLogger('statbox').info({
                        'action': 'rescheduled',
                        'mode': 'reschedule_subscriptions',
                        'sql': update_sql,
                    })

        return response_pb
