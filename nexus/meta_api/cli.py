import fire
from nexus.meta_api.aioclient import MetaApiGrpcClient


async def client(endpoint):
    client = MetaApiGrpcClient(endpoint)
    return client.get_interface()


if __name__ == '__main__':
    fire.Fire(client)
