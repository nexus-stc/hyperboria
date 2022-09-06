from __future__ import annotations

import asyncio.exceptions
from typing import Iterable

from aiokit import AioThing
from izihawa_utils.importlib import instantiate_object
from tenacity import (
    retry,
    retry_if_exception_type,
    wait_fixed,
)


class Processor(AioThing):
    def filter(self, message) -> bool:
        return True

    async def process(self, message):
        return message

    async def process_bulk(self, messages: Iterable):
        for message in messages:
            await self.process(message)


class ActionProcessor(Processor):
    def __init__(self, actions, filter):
        super().__init__()
        self.actions = [instantiate_object(action) for action in actions]
        self.filter_object = instantiate_object(filter)
        self.starts.append(self.filter_object)
        self.starts.extend(self.actions)

    def filter(self, message) -> bool:
        return self.filter_object.filter(message)

    @retry(retry=retry_if_exception_type(asyncio.exceptions.TimeoutError), wait=wait_fixed(5))
    async def process(self, message):
        for action in self.actions:
            message = await action.do(message)
