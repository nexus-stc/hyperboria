import asyncio
from typing import Iterable

from aiokafka import AIOKafkaProducer

from .base import BaseSink


class KafkaSink(BaseSink):
    def __init__(self, kafka_hosts: Iterable[str], topic_name: str):
        super().__init__()
        self.producer = AIOKafkaProducer(
            loop=asyncio.get_event_loop(),
            bootstrap_servers=kafka_hosts,
        )
        self.topic_name = topic_name
        self.starts.append(self.producer)

    async def send(self, data: bytes):
        await self.producer.send_and_wait(
            self.topic_name,
            data,
        )
