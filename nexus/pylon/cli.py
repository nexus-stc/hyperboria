import logging
import os
import sys

import fire
from aiokit.utils import sync_fu
from nexus.pylon.client import (
    DownloadError,
    PylonClient,
)
from nexus.pylon.configs import get_config
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
                    print(f'Started transmission from {resp.source}...', end='\r', file=sys.stderr)
                    last_len = 0
                    last_source = resp.source
                    collected = bytes()
            elif resp.HasField('chunk'):
                if len(collected) - last_len > 1024 * 100:
                    print(f'Loaded {len(collected)} bytes from {resp.source}', end='\r', file=sys.stderr)
                    last_len = len(collected)
                    last_source = resp.source
                collected += resp.chunk.content
        with open(resolve_path(output), 'wb') as f:
            print(f'Completed! Loaded {len(collected)} bytes from {last_source}', file=sys.stderr)
            f.write(collected)
    except DownloadError:
        print('File not found')


async def download(
    output: str,
    debug: bool = False,
    **params,
):
    if debug:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    c = get_config()['pylon']
    p = PylonClient(
        proxies=c['proxies'],
        source_configs=c['sources'],
        default_driver_proxy_list=c['default_driver_proxy_list'],
        downloads_directory=c['downloads_directory'],
    )
    return await fetch(iter=p.download(params=params), output=output)


def main():
    fire.Fire({
        'download': sync_fu(download),
    })


if __name__ == '__main__':
    main()
