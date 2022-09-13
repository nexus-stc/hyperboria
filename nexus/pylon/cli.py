import logging
import os
import sys
from typing import Optional

import fire
from aiokit.utils import sync_fu
from izihawa_configurator import Configurator

from .client import (
    DownloadError,
    PylonClient,
)
from .proto.file_pb2 import FileResponse as FileResponsePb


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
        async for resp in iter:
            if resp.HasField('status'):
                if resp.status == FileResponsePb.Status.BEGIN_TRANSMISSION:
                    print(f'Started transmission...', file=sys.stderr)
                    last_len = 0
                    collected = bytes()
            elif resp.HasField('chunk'):
                if len(collected) - last_len > 1024 * 100:
                    print(f'Loaded {len(collected)} bytes', end='\r', file=sys.stderr)
                    last_len = len(collected)
                collected += resp.chunk.content
        with open(resolve_path(output), 'wb') as f:
            print()
            print(f'Completed! Loaded {len(collected)} bytes', file=sys.stderr)
            f.write(collected)
    except DownloadError:
        print('File not found')


async def download(
    output: str,
    config: Optional[str] = None,
    debug: bool = False,
    wd_endpoint: Optional[str] = None,
    wd_directory: Optional[str] = None,
    wd_host_directory: Optional[str] = None,
    **params,
):
    """
    Download scientific publications from various sources
    Large portion of fresh articles could be retrieved only though publisher libraries through `BrowserDriver`, it
    requires Selenium webdriver:
    `docker run -e SE_START_XVFB=false -v $(pwd)/downloads:/downloads -p 4444:4444 selenium/standalone-chrome:latest`
    Args:
        output: name of the output file
        config: pylon config
        debug: enable debug logging
        wd_endpoint: web-driver
        wd_directory: mounted directory inside Docker image
        wd_host_directory: directory for downloads on host that should be mounter as `wd_directory` inside Docker image
    """
    if debug:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    default_config_path = os.path.join(os.path.dirname(__file__), 'configs/pylon.yaml')
    config = Configurator([config if config else default_config_path], env_prefix='NEXUS_PYLON')
    config = config['pylon']
    if wd_endpoint:
        config.setdefault('webdriver_hub', {})
        config['webdriver_hub']['endpoint'] = wd_endpoint
        if not wd_directory:
            raise ValueError('Should pass --wd-directory with --wd-endpoint')
        config['webdriver_hub']['downloads_directory'] = wd_directory
        if not wd_host_directory:
            raise ValueError('Should pass --wd-host-directory with --wd-endpoint')
        config['webdriver_hub']['host_downloads_directory'] = wd_host_directory

    pylon_client = PylonClient(config=config)
    return await fetch(iter=pylon_client.download(params=params), output=output)


def main():
    try:
        fire.Fire({
            'download': sync_fu(download),
        })
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
