import asyncio
import hashlib
import logging
import time
from datetime import (
    datetime,
    timedelta,
)

from aiogrobid.exceptions import BadRequestError
from grpc import ServicerContext
from idm.api.proto import subscription_manager_service_pb2
from izihawa_utils.common import filter_none
from izihawa_utils.pb_to_json import MessageToDict
from library.aiogrpctools.base import aiogrpc_request_wrapper
from library.telegram.base import RequestContext
from library.telegram.utils import safe_execution
from nexus.hub.fancy_names import get_fancy_name
from nexus.hub.proto import (
    delivery_service_pb2,
    delivery_service_pb2_grpc,
)
from nexus.models.proto.operation_pb2 import \
    DocumentOperation as DocumentOperationPb
from nexus.models.proto.operation_pb2 import \
    StoreTelegramFileId as StoreTelegramFileIdPb
from nexus.models.proto.operation_pb2 import UpdateDocument as UpdateDocumentPb
from nexus.pylon.client import PylonClient
from nexus.pylon.exceptions import DownloadError
from nexus.pylon.pdftools import clean_metadata
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from nexus.translations import t
from nexus.views.telegram.base_holder import (
    BaseHolder,
    ScimagHolder,
)
from nexus.views.telegram.progress_bar import (
    ProgressBar,
    ProgressBarLostMessageError,
)
from prometheus_client import Gauge
from pypika import (
    PostgreSQLQuery,
    Table,
)

from .base import (
    BaseHubService,
    ProcessedDocument,
    is_group_or_channel,
)

downloads_gauge = Gauge('downloads_total', documentation='Currently downloading files')


async def operation_log(document_operation_pb):
    logging.getLogger('operation').info(msg=MessageToDict(document_operation_pb, preserving_proto_field_name=True))


class DeliveryService(delivery_service_pb2_grpc.DeliveryServicer, BaseHubService):
    def __init__(
        self,
        application,
        service_name: str,
        is_sharience_enabled: bool,
        maintenance_picture_url: str,
        should_parse_with_grobid: bool,
        should_store_hashes: bool,
        telegram_bot_configs: dict,
        pylon_config: dict,
    ):
        super().__init__(application=application, service_name=service_name)
        self.downloadings = set()
        self.is_sharience_enabled = is_sharience_enabled
        self.maintenance_picture_url = maintenance_picture_url
        self.pylon_client = PylonClient(config=pylon_config)
        self.should_parse_with_grobid = should_parse_with_grobid
        self.should_store_hashes = should_store_hashes
        self.telegram_bot_configs = telegram_bot_configs
        self.starts.extend([self.pylon_client])

    async def start(self):
        delivery_service_pb2_grpc.add_DeliveryServicer_to_server(self, self.application.server)

    async def stop(self):
        for download in set(self.downloadings):
            await download.external_cancel()
        await asyncio.gather(*map(lambda x: x.task, self.downloadings))

    async def get_telegram_file_id(self, document_id):
        telegram_files = Table('telegram_files')
        query = PostgreSQLQuery.from_('telegram_files').select(
            telegram_files.bot_name,
            telegram_files.telegram_file_id,
        ).where(telegram_files.document_id == document_id)
        pg_data = self.application.pool_holder.iterate(query.get_sql())
        bot_files = {}
        async for bot_name, telegram_file_id in pg_data:
            bot_files[bot_name] = telegram_file_id
        return bot_files

    @aiogrpc_request_wrapper(log=False)
    async def get_availability_data(
        self,
        request: delivery_service_pb2.GetAvailabilityDataRequest,
        context: ServicerContext,
        metadata: dict,
    ) -> delivery_service_pb2.GetAvailabilityDataResponse:
        return delivery_service_pb2.GetAvailabilityDataResponse(
            bot_files=await self.get_telegram_file_id(request.document_id),
        )

    @aiogrpc_request_wrapper(log=False)
    async def start_delivery(
        self,
        request: delivery_service_pb2.StartDeliveryRequest,
        context: ServicerContext,
        metadata: dict,
    ) -> delivery_service_pb2.StartDeliveryResponse:
        document_holder = BaseHolder.create(request.typed_document)
        request_context = RequestContext(
            bot_name=request.bot_name,
            chat=request.chat,
            request_id=metadata.get('request-id'),
        )
        request_context.add_default_fields(
            mode='delivery',
            session_id=metadata.get('session-id'),
            document_id=document_holder.id,
            index_alias=document_holder.index_alias,
            **self.get_default_service_fields(),
        )
        if document_holder.doi:
            request_context.add_default_fields(doi=document_holder.doi)

        telegram_file_id = None
        if self.telegram_bot_configs[request_context.bot_name]['should_use_telegram_file_id']:
            bot_files = await self.get_telegram_file_id(document_holder.id)
            telegram_file_id = bot_files.get(request_context.bot_name)
        if telegram_file_id:
            try:
                async with safe_execution(error_log=request_context.error_log):
                    await self.send_file(
                        document_holder=document_holder,
                        file=telegram_file_id,
                        session_id=metadata.get('session-id'),
                        request_context=request_context,
                        voting=not is_group_or_channel(request_context.chat.chat_id),
                    )
                    request_context.statbox(action='cache_hit')
            except ValueError:
                telegram_file_id = None
        if not telegram_file_id:
            if self.application.user_manager.has_task(request.chat.chat_id, document_holder.id):
                return delivery_service_pb2.StartDeliveryResponse(status=delivery_service_pb2.StartDeliveryResponse.Status.ALREADY_DOWNLOADING)
            if self.application.user_manager.hit_limits(request.chat.chat_id):
                return delivery_service_pb2.StartDeliveryResponse(status=delivery_service_pb2.StartDeliveryResponse.Status.TOO_MANY_DOWNLOADS)
            await DownloadTask(
                delivery_service=self,
                document_holder=document_holder,
                request_context=request_context,
                session_id=metadata.get('session-id'),
            ).schedule()
        return delivery_service_pb2.StartDeliveryResponse(status=delivery_service_pb2.StartDeliveryResponse.Status.OK)


async def delayed_task(create_task, t):
    try:
        await asyncio.sleep(t)
        task = create_task()
        await task
    except asyncio.CancelledError:
        pass


class DownloadTask:
    def __init__(
        self,
        delivery_service,
        request_context,
        document_holder,
        session_id: str,
    ):
        self.application = delivery_service.application
        self.delivery_service = delivery_service
        self.request_context = request_context
        self.document_holder = document_holder
        self.session_id = session_id
        self.task = None

    async def schedule(self):
        self.delivery_service.downloadings.add(self)
        self.application.user_manager.add_task(self.request_context.chat.chat_id, self.document_holder.id)
        self.task = asyncio.create_task(
            self.download_task(
                request_context=self.request_context,
                document_holder=self.document_holder,
            )
        )
        self.task.add_done_callback(self.done_callback)

    def done_callback(self, f):
        self.delivery_service.downloadings.remove(self)
        self.application.user_manager.remove_task(
            self.request_context.chat.chat_id,
            self.document_holder.id,
        )

    async def download_task(self, request_context: RequestContext, document_holder):
        throttle_secs = 3.0

        async def _on_fail():
            await self.application.telegram_clients[request_context.bot_name].send_message(
                request_context.chat.chat_id,
                t('MAINTENANCE', request_context.chat.language).format(
                    maintenance_picture_url=self.delivery_service.maintenance_picture_url
                ),
                buttons=request_context.personal_buttons()
            )
        async with safe_execution(
            error_log=request_context.error_log,
            on_fail=_on_fail,
        ):
            start_time = time.time()
            filename = document_holder.get_filename()
            progress_bar_download = ProgressBar(
                telegram_client=self.application.telegram_clients[request_context.bot_name],
                request_context=request_context,
                banner=t("LOOKING_AT", request_context.chat.language),
                header=f'⬇️ {filename}',
                tail_text=t('TRANSMITTED_FROM', request_context.chat.language),
                throttle_secs=throttle_secs,
                last_call=start_time,
            )
            downloads_gauge.inc()
            try:
                file = await self.download(
                    document_holder=document_holder,
                    progress_bar=progress_bar_download,
                )
                if file:
                    request_context.statbox(
                        action='downloaded',
                        duration=time.time() - start_time,
                        len=len(file),
                    )
                    if not document_holder.md5 and document_holder.get_extension() == 'pdf':
                        try:
                            processing_message_task = asyncio.create_task(delayed_task(
                                create_task=lambda: progress_bar_download.send_message(
                                    t("PROCESSING_PAPER", request_context.chat.language).format(filename=filename),
                                    ignore_last_call=True
                                ),
                                t=5.0
                            ))
                            file = await asyncio.get_running_loop().run_in_executor(
                                None,
                                lambda: clean_metadata(file, doi=document_holder.doi)
                            )

                            processing_message_task.cancel()
                            await processing_message_task

                            request_context.statbox(
                                action='cleaned',
                                len=len(file),
                            )
                        except ValueError as e:
                            request_context.error_log(e)
                    progress_bar_upload = ProgressBar(
                        telegram_client=self.application.telegram_clients[request_context.bot_name],
                        request_context=request_context,
                        message=progress_bar_download.message,
                        banner=t("LOOKING_AT", request_context.chat.language),
                        header=f'⬇️ {filename}',
                        tail_text=t('UPLOADED_TO_TELEGRAM', request_context.chat.language),
                        throttle_secs=throttle_secs,
                        last_call=progress_bar_download.last_call,
                    )
                    uploaded_message = await self.delivery_service.send_file(
                        document_holder=self.document_holder,
                        file=file,
                        progress_callback=progress_bar_upload.callback,
                        request_context=self.request_context,
                        session_id=self.session_id,
                        voting=not is_group_or_channel(self.request_context.chat.chat_id),
                    )
                    if self.document_holder.doi:
                        await self.delivery_service.found_item(
                            bot_name=request_context.bot_name,
                            doi=self.document_holder.doi,
                        )
                    request_context.statbox(
                        action='uploaded',
                        duration=time.time() - start_time,
                    )
                    asyncio.create_task(self.store_new_data(
                        bot_name=request_context.bot_name,
                        document_holder=document_holder,
                        telegram_file_id=uploaded_message.file.id,
                        file=file,
                        request_context=request_context,
                    ))
                else:
                    request_context.statbox(
                        action='missed',
                        duration=time.time() - start_time,
                    )

                    if self.delivery_service.is_sharience_enabled and await self.try_sharience(
                        request_context=request_context,
                        document_holder=document_holder,
                    ):
                        return

                    request_context.statbox(
                        action='not_found',
                        duration=time.time() - start_time,
                    )
                    await self.respond_not_found(
                        request_context=request_context,
                        document_holder=document_holder,
                    )
            except DownloadError:
                await self.external_cancel()
            except ProgressBarLostMessageError:
                self.request_context.statbox(
                    action='user_canceled',
                    duration=time.time() - start_time,
                )
            except asyncio.CancelledError:
                request_context.statbox(action='canceled')
            finally:
                downloads_gauge.dec()
                messages = filter_none([progress_bar_download.message])
                if messages:
                    async with safe_execution(error_log=request_context.error_log):
                        await self.application.telegram_clients[request_context.bot_name].delete_messages(
                            request_context.chat.chat_id,
                            messages
                        )
                request_context.debug_log(action='deleted_progress_message')

    async def process_resp(self, resp, progress_bar, collected, filesize):
        progress_bar.set_source(get_fancy_name(resp.source))
        if resp.HasField('status'):
            if resp.status == FileResponsePb.Status.RESOLVING:
                await progress_bar.show_banner()
            if resp.status == FileResponsePb.Status.BEGIN_TRANSMISSION:
                collected.clear()
        elif resp.HasField('chunk'):
            collected.extend(resp.chunk.content)
            await progress_bar.callback(len(collected), filesize)

    async def respond_not_found(self, request_context: RequestContext, document_holder):
        if (
            isinstance(document_holder, ScimagHolder)
            and document_holder.doi
        ):
            await self.application.idm_client.subscribe(
                chat_id=request_context.chat.chat_id,
                subscription_query=f'doi:{document_holder.doi}',
                schedule='0 * * * *',
                is_oneshot=True,
                is_downloadable=True,
                request_id=request_context.request_id,
                session_id=self.session_id,
                valid_until=int(time.mktime((datetime.now() + timedelta(days=7)).timetuple())),
                subscription_type=subscription_manager_service_pb2.Subscription.Type.DOI
            )
            if mutual_aid_service := self.application.mutual_aid_services.get(request_context.bot_name):
                await mutual_aid_service.request(document_holder.doi, document_holder.type)
        return await self.application.telegram_clients[request_context.bot_name].send_message(
            request_context.chat.chat_id,
            t("SOURCES_UNAVAILABLE", request_context.chat.language).format(
                document=document_holder.doi or document_holder.view_builder(
                    request_context.chat.language).add_title(bold=False).build()
            ),
            buttons=request_context.personal_buttons()
        )

    async def try_sharience(self, request_context, document_holder):
        if document_holder.doi:
            request_context.statbox(action='try_sharience')
            pg_data = self.application.pool_holder.iterate(
                '''
                select sh.id, t.telegram_file_id as vote_sum
                from sharience as sh
                left join votes as v
                on sh.id = v.document_id
                left join telegram_files as t
                on sh.parent_id = t.document_id
                where t.bot_name = %s
                group by sh.id, t.telegram_file_id
                having coalesce(sum(v.value), 0) > -1
                and sh.parent_id = %s
                order by coalesce(sum(v.value), 0) desc;
                ''', (self.request_context.bot_name, document_holder.id,))
            async for document_id, telegram_file_id in pg_data:
                return await self.delivery_service.send_file(
                    document_id=document_id,
                    document_holder=self.document_holder,
                    file=telegram_file_id,
                    request_context=self.request_context,
                    session_id=self.session_id,
                    voting=True,
                )

    async def download(self, document_holder, progress_bar):
        collected = bytearray()
        params = {}
        try:
            if document_holder.doi:
                params['doi'] = document_holder.doi
            if document_holder.md5:
                params['md5'] = document_holder.md5
            if document_holder.ipfs_multihashes:
                params['ipfs_multihashes'] = [ipfs_multihash for ipfs_multihash in document_holder.ipfs_multihashes]
            if params:
                async for resp in self.delivery_service.pylon_client.download(params):
                    await self.process_resp(
                        resp=resp,
                        progress_bar=progress_bar,
                        collected=collected,
                        filesize=document_holder.filesize,
                    )
                return bytes(collected)
        except DownloadError:
            pass

    async def external_cancel(self):
        self.request_context.statbox(action='externally_canceled')
        await self.application.telegram_clients[self.request_context.bot_name].send_message(
            self.request_context.chat.chat_id,
            t("DOWNLOAD_CANCELED", self.request_context.chat.language).format(
                document=self.document_holder.view_builder(self.request_context.chat.language).add_title(bold=False).build()
            ),
            buttons=self.request_context.personal_buttons()
        )
        self.task.cancel()
        await self.task

    async def store_new_data(self, bot_name, document_holder, telegram_file_id, file, request_context):
        document_pb = document_holder.document_pb
        new_fields = []
        if self.delivery_service.should_store_hashes:
            document_pb.filesize = len(file)
            if not document_pb.md5:
                document_pb.md5 = hashlib.md5(file).hexdigest()
            del document_pb.ipfs_multihashes[:]
            document_pb.ipfs_multihashes.extend(await self.delivery_service.get_ipfs_hashes(file=file))
            new_fields.extend(['filesize', 'ipfs_multihashes', 'md5'])
            store_telegram_file_id_operation_pb = DocumentOperationPb(
                store_telegram_file_id=StoreTelegramFileIdPb(
                    document_id=document_pb.id,
                    telegram_file_id=telegram_file_id,
                    bot_name=bot_name,
                ),
            )
            await operation_log(store_telegram_file_id_operation_pb),
        if (
            self.delivery_service.should_parse_with_grobid
            and document_holder.index_alias == 'scimag'
        ):
            try:
                processed_document = await ProcessedDocument.setup(
                    file,
                    grobid_client=self.application.grobid_client,
                    request_context=request_context,
                )
                new_fields += self.delivery_service.set_fields_from_processed(document_pb, processed_document)
            except BadRequestError as e:
                self.request_context.statbox(action='unparsable_document')
                self.request_context.error_log(e)

        if new_fields:
            update_document_operation_pb = DocumentOperationPb(
                update_document=UpdateDocumentPb(
                    full_text_index=True,
                    fields=new_fields,
                    typed_document=document_holder.get_typed_document(),
                ),
            )
            await operation_log(update_document_operation_pb)
