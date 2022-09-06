import asyncio

from aiokafka import AIOKafkaProducer

from .base import BaseSink


class KafkaSink(BaseSink):
    def __init__(self, kafka, topic_name):
        super().__init__()
        self.kafka = kafka
        self.topic_name = topic_name
        self.producer = AIOKafkaProducer(
            loop=asyncio.get_event_loop(),
            bootstrap_servers=kafka['bootstrap_servers'],
            max_request_size=kafka['max_request_size'],
        )
        self.starts.append(self.producer)

    async def send(self, data: bytes):
        await self.producer.send_and_wait(
            self.topic_name,
            data,
        )
