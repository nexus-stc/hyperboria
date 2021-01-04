from aiokit import AioThing


class BaseAction(AioThing):
    async def do(self, item):
        pass
