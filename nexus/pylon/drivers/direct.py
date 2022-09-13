import logging
from typing import Dict

import aiohttp.client_exceptions
from aiohttp_socks import ProxyError
from nexus.pylon.drivers.base import BaseDriver
from nexus.pylon.exceptions import (
    BadResponseError,
    NotFoundError,
)
from nexus.pylon.prepared_request import PreparedRequest
from nexus.pylon.proto.file_pb2 import Chunk as ChunkPb
from nexus.pylon.proto.file_pb2 import FileResponse as FileResponsePb
from python_socks import ProxyTimeoutError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random,
)


class DirectDriver(BaseDriver):
    allowed_content_type = None

    @retry(
        reraise=True,
        wait=wait_random(min=1, max=2),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type((ProxyError, aiohttp.client_exceptions.ClientPayloadError, ProxyTimeoutError)),
    )
    async def execute_prepared_file_request(self, prepared_file_request: PreparedRequest, params: Dict):
        logging.debug({
            'action': 'download',
            'mode': 'pylon',
            'params': params,
            'source': str(self),
            'url': prepared_file_request.url,
        })
        async with self.get_session() as session:
            async with prepared_file_request.execute_with(session=session) as resp:
                logging.debug({
                    'action': 'response',
                    'mode': 'pylon',
                    'params': params,
                    'source': str(self),
                    'url': prepared_file_request.url,
                    'status': resp.status,
                })
                if resp.status == 404:
                    raise NotFoundError(url=prepared_file_request.url)
                elif (
                    resp.status != 200
                    or (
                        self.allowed_content_type
                        and resp.headers.get('Content-Type', '').lower() not in self.allowed_content_type
                    )
                ):
                    raise BadResponseError(
                        request_headers=prepared_file_request.headers,
                        url=prepared_file_request.url,
                        status=resp.status,
                        headers=str(resp.headers),
                    )
                file_validator = self.validator(params)
                yield FileResponsePb(status=FileResponsePb.Status.BEGIN_TRANSMISSION, source=prepared_file_request.url)
                async for content, _ in resp.content.iter_chunks():
                    file_validator.update(content)
                    yield FileResponsePb(chunk=ChunkPb(content=content), source=prepared_file_request.url)
                file_validator.validate()
