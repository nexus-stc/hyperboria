from aiokit import AioThing


class Rescorer(AioThing):
    def __init__(self, learn_logger=None, executor=None):
        super().__init__()
        self.learn_logger = learn_logger
        self.executor = executor

    async def rescore(self, document_pbs, query, session_id, language):
        raise NotImplementedError()
