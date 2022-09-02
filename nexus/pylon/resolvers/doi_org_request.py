import json
import logging
from typing import (
    AsyncIterable,
    Dict,
    List,
    Optional,
)

import jq
from nexus.pylon.prepared_request import PreparedRequest
from nexus.pylon.proxy_manager import ProxyManager
from nexus.pylon.resolvers.base import BaseResolver


class DoiOrgRequestResolver(BaseResolver):
    def __init__(
        self,
        selector='.link[0].URL',
        format_string='{selected}',
        timeout: float = 10.0,
        resolve_timeout: float = 10.0,
        proxy_list: Optional[List] = None,
        proxy_manager: Optional[ProxyManager] = None,
    ):
        super().__init__(proxy_list=proxy_list, proxy_manager=proxy_manager)
        self.selector = jq.compile(selector)
        self.format_string = format_string
        self.timeout = timeout
        self.resolve_timeout = resolve_timeout

    def __str__(self):
        return f'{self.__class__.__name__}(selector = {self.selector}, format_string = {self.format_string})'

    async def resolve_through_doi_org(self, params):
        async with self.get_session() as session:
            doi_url = f'https://doi.org/{params["doi"]}'
            async with PreparedRequest(
                method='get',
                url=doi_url,
                timeout=self.resolve_timeout,
                headers={'Accept': 'application/json'}
            ).execute_with(session=session) as resp:
                return await resp.json()

    async def resolve(self, params: Dict) -> AsyncIterable[PreparedRequest]:
        body = await self.resolve_through_doi_org(params)
        try:
            selected = json.loads(self.selector.input(body).text())
        except ValueError as e:
            logging.getLogger('error').error({
                'action': 'error',
                'mode': 'pylon',
                'error': str(e)
            })
            return
        if selected:
            yield PreparedRequest(
                method='get',
                url=self.format_string.format(selected=selected),
                timeout=self.timeout,
            )
