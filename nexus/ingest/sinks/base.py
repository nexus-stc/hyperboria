from aiokit import AioThing


class BaseSink(AioThing):
    def __init__(self):
        super().__init__()

    def send(self, data: bytes):
        raise NotImplementedError()

    async def on_shutdown(self):
        pass
