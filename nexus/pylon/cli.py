import os
from typing import Optional

import fire
from aiokit.utils import sync_fu
from nexus.pylon.client import (
    DownloadError,
    PylonClient,
)
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb


def resolve_path(filepath):
    if os.path.isabs(filepath):
        return filepath
    cwd = os.environ.get('BUILD_WORKING_DIRECTORY', os.getcwd())
    filepath = os.path.join(cwd, filepath)
    return filepath


async def fetch(
    iter,
    output: str,
):
    collected = bytes()
    try:
        last_len = 0
        last_source = ''
        async for resp in iter:
            if resp.HasField('status'):
                if resp.status == FileResponsePb.Status.BEGIN_TRANSMISSION:
                    print(f'Started transmission from {resp.source}...', end='\r')
                    last_len = 0
                    last_source = resp.source
                    collected = bytes()
            elif resp.HasField('chunk'):
                if len(collected) - last_len > 1024 * 100:
                    print(f'Loaded {len(collected)} bytes from {resp.source}', end='\r')
                    last_len = len(collected)
                    last_source = resp.source
                collected += resp.chunk.content
        with open(resolve_path(output), 'wb') as f:
            print(f'Completed! Loaded {len(collected)} bytes from {last_source}')
            f.write(collected)
    except DownloadError:
        print('File not found')


async def fetch_by_md5(
    md5: str,
    output: str,
    proxy: Optional[str] = None,
    resolve_proxy: Optional[str] = None,
):
    if proxy and not resolve_proxy:
        resolve_proxy = proxy
    p = PylonClient(proxy=proxy, resolve_proxy=resolve_proxy)
    return await fetch(iter=p.by_md5(md5=md5), output=output)


async def fetch_by_doi(
    doi: str,
    output: str,
    proxy: Optional[str] = None,
    resolve_proxy: Optional[str] = None,
):
    if proxy and not resolve_proxy:
        resolve_proxy = proxy
    p = PylonClient(proxy=proxy, resolve_proxy=resolve_proxy)
    return await fetch(iter=p.by_doi(doi=doi), output=output)


def main():
    fire.Fire({
        'doi': sync_fu(fetch_by_doi),
        'md5': sync_fu(fetch_by_md5),
    })


if __name__ == '__main__':
    main()
