import fire
from aiokit.utils import sync_fu
from nexus.meta_api.aioclient import MetaApiGrpcClient


async def search(endpoint, index_alias, query):
    client = MetaApiGrpcClient(endpoint)
    try:
        await client.start()
        print(await client.search(index_aliases=(index_alias,), query=query, language='ru'))
    finally:
        await client.stop()


if __name__ == '__main__':
    fire.Fire(sync_fu(search))
