import logging
from functools import wraps

from aiokit import (
    AioRootThing,
    AioThing,
)
from google.protobuf.json_format import MessageToDict
from grpc import aio
from izihawa_utils.text import camel_to_snake
from library.logging import error_log


class AioGrpcServer(AioRootThing):
    def __init__(self, address, port):
        super().__init__()
        self.server = aio.server()
        self.server.add_insecure_port(f'{address}:{port}')

    async def start(self):
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self):
        await self.server.stop(None)


class BaseService(AioThing):
    error_mapping = {}

    def __init__(self, service_name):
        super().__init__()
        self.service_name = service_name
        self.class_name = camel_to_snake(self.__class__.__name__)

    def get_default_service_fields(self):
        return {'service_name': self.service_name, 'view': self.class_name}

    def statbox(self, **kwargs):
        logging.getLogger('statbox').info(self.get_default_service_fields() | kwargs)


def aiogrpc_request_wrapper(log=True):
    def _aiogrpc_request_wrapper(func):
        @wraps(func)
        async def wrapped(self, request, context):
            metadata = dict(context.invocation_metadata())
            try:
                if log:
                    self.statbox(
                        action='enter',
                        mode=func.__name__,
                        request_id=metadata['request-id'],
                    )
                r = await func(self, request, context, metadata)
                if log:
                    self.statbox(
                        action='exit',
                        mode=func.__name__,
                        request_id=metadata['request-id'],
                    )
                return r
            except aio.AbortError:
                raise
            except Exception as e:
                serialized_request = MessageToDict(request, preserving_proto_field_name=True)
                error_log(e, request=serialized_request, request_id=metadata['request-id'])
                if e.__class__ in self.error_mapping:
                    await context.abort(*self.error_mapping[e.__class__])
                raise e
        return wrapped
    return _aiogrpc_request_wrapper


def aiogrpc_streaming_request_wrapper(func):
    @wraps(func)
    async def wrapped(self, request, context):
        metadata = dict(context.invocation_metadata())
        try:
            self.statbox(
                action='enter',
                mode=func.__name__,
                request_id=metadata['request-id'],
            )
            async for item in func(self, request, context, metadata):
                yield item
            self.statbox(
                action='exit',
                mode=func.__name__,
                request_id=metadata['request-id'],
            )
        except aio.AbortError:
            raise
        except Exception as e:
            serialized_request = MessageToDict(request, preserving_proto_field_name=True)
            error_log(e, request=serialized_request, request_id=metadata['request-id'])
            if e.__class__ in self.error_mapping:
                await context.abort(*self.error_mapping[e.__class__])
            raise e
    return wrapped
