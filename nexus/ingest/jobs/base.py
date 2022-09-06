from typing import (
    Any,
    AsyncIterable,
    Iterable,
    Union,
)

from aiokit import AioRootThing
from izihawa_utils.importlib import import_object

from ..sinks.base import BaseSink


class BaseJob(AioRootThing):
    name = None

    def __init__(self, actions: Iterable[dict], sinks: Iterable[Union[dict, BaseSink]]):
        super().__init__()
        real_sinks = []
        for sink in sinks:
            if isinstance(sink, BaseSink):
                real_sinks.append(sink)
            else:
                real_sinks.append(import_object(sink['class'])(**sink.get('kwargs', {})))
        self.sinks = real_sinks

        real_actions = []
        for action in actions:
            real_actions.append(import_object(action['class'])(**action.get('kwargs', {})))
        self.actions = real_actions

        self.starts.extend(self.sinks)
        self.starts.extend(self.actions)

    async def iterator(self) -> AsyncIterable[Any]:
        raise NotImplementedError()

    async def action_iterator(self) -> AsyncIterable[Any]:
        async for item in self.iterator():
            processed_item = item
            for action in self.actions:
                processed_item = await action.do(processed_item)
            yield processed_item

    async def start(self):
        async for data in self.action_iterator():
            for sink in self.sinks:
                await sink.send(data)
