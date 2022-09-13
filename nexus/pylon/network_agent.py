import socket
from random import choice
from sys import platform
from typing import (
    List,
    Optional,
)

import aiohttp
from aiohttp import ClientSession
from aiohttp.client_reqrep import ClientRequest
from aiohttp_socks import ProxyConnector
from aiokit import AioThing
from nexus.pylon.proxy_manager import (
    AllOf,
    AnyOf,
    ProxyManager,
)


class KeepAliveClientRequest(ClientRequest):
    async def send(self, conn):
        sock = conn.protocol.transport.get_extra_info('socket')
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        if platform != 'darwin':
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 2)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)

        return await super().send(conn)


class NetworkAgent(AioThing):
    def __init__(
        self,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        super().__init__()
        self.proxy_list = []
        if proxy_list:
            if not isinstance(proxy_list, list):
                proxy_list = [proxy_list]
            for proxy_tags in proxy_list:
                if isinstance(proxy_tags, list):
                    self.proxy_list.append(AnyOf(set(proxy_tags)))
                elif isinstance(proxy_tags, dict) and 'any_of' in proxy_tags:
                    self.proxy_list.append(AnyOf(set(proxy_tags['any_of'])))
                elif isinstance(proxy_tags, dict) and 'all_of' in proxy_tags:
                    self.proxy_list.append(AllOf(set(proxy_tags['all_of'])))
        self.proxy_manager = proxy_manager

    def get_session(self) -> ClientSession:
        connector = None
        if self.proxy_list and self.proxy_manager:
            if proxy := self.proxy_manager.get_proxy(choice(self.proxy_list)):
                connector = ProxyConnector.from_url(proxy.get_address())
        if not connector:
            connector = aiohttp.TCPConnector()
        return aiohttp.ClientSession(request_class=KeepAliveClientRequest, connector=connector)
