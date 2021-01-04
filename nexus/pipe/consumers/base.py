from __future__ import annotations

import asyncio
import logging
from typing import (
    List,
    Union,
)

import orjson as json
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import (
    CommitFailedError,
    ConsumerStoppedError,
)
from aiokit import AioRootThing
from google.protobuf.json_format import ParseDict
from nexus.actions.exceptions import (
    ConflictError,
    InterruptProcessing,
)
from nexus.pipe.processors.base import Processor


class BaseConsumer(AioRootThing):
    def __init__(self, processors: List[Processor],
                 topic_names: Union[str, List[str]], bootstrap_servers: str, group_id: str):
        super().__init__()
        self.processors = processors
        if isinstance(topic_names, str):
            topic_names = [topic_names]
        self.topic_names = topic_names
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.consumer = None
        self.starts.extend(self.processors)

    def create_consumer(self):
        return AIOKafkaConsumer(
            *self.topic_names,
            auto_offset_reset='earliest',
            loop=asyncio.get_event_loop(),
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            enable_auto_commit=False,
        )

    def preprocess(self, msg):
        return msg

    async def start(self):
        logging.getLogger('statbox').info({
            'action': 'started',
            'group_id': self.group_id,
            'topic_names': self.topic_names,
        })
        self.consumer = self.create_consumer()
        await self.consumer.start()
        try:
            async for msg in self.consumer:
                preprocessed_msg = self.preprocess(msg)
                if preprocessed_msg:
                    for processor in self.processors:
                        if not processor.filter(preprocessed_msg):
                            continue
                        try:
                            await processor.process(preprocessed_msg)
                        except (ConflictError, InterruptProcessing) as e:
                            logging.getLogger('statbox').info(e)
                        except Exception as e:
                            logging.getLogger('error').error(e)
                            raise
                try:
                    await self.consumer.commit()
                except CommitFailedError as e:
                    logging.getLogger('error').error(e)
        except ConsumerStoppedError:
            pass

    async def stop(self):
        if not self.consumer:
            return
        await self.consumer.stop()


class BasePbConsumer(BaseConsumer):
    pb_class = None

    def preprocess(self, msg) -> pb_class:
        pb = self.pb_class()
        pb.ParseFromString(msg.value)
        return pb


class BaseJsonConsumer(BaseConsumer):
    pb_class = None

    def preprocess(self, msg) -> pb_class:
        pb = self.pb_class()
        message = json.loads(msg.value)
        ParseDict(message, pb, ignore_unknown_fields=True)
        return pb


class BaseBulkConsumer(BaseConsumer):
    bulk_size = 20
    timeout = 1

    async def start(self):
        logging.getLogger('statbox').info({
            'action': 'started',
            'group_id': self.group_id,
            'topic_names': self.topic_names,
        })
        self.consumer = self.create_consumer()
        await self.consumer.start()
        while self.started:
            try:
                result = await self.consumer.getmany(timeout_ms=self.timeout * 1000, max_records=self.bulk_size)
            except ConsumerStoppedError:
                break
            collector = []
            for tp, messages in result.items():
                if messages:
                    for message in messages:
                        preprocessed_msg = self.preprocess(message)
                        if preprocessed_msg:
                            collector.append(preprocessed_msg)
            for processor in self.processors:
                filtered = filter(processor.filter, collector)
                try:
                    await processor.process_bulk(filtered)
                except InterruptProcessing as e:
                    logging.getLogger('statbox').info(e)
                except Exception as e:
                    logging.getLogger('error').error(e)
                    raise
            try:
                await self.consumer.commit()
            except CommitFailedError as e:
                logging.getLogger('error').error(e)
                continue
