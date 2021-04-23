import fire
from aiokit.utils import sync_fu
from nexus.meta_api.aioclient import MetaApiGrpcClient


async def search(url, schema, query):
    client = MetaApiGrpcClient(url)
    try:
        await client.start()
        print(await client.search(schemas=(schema,), query=query, language='ru'))
    finally:
        await client.stop()


if __name__ == '__main__':
    fire.Fire(sync_fu(search))
