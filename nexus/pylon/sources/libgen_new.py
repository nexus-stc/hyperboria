import re
from typing import AsyncIterable

from library.logging import error_log
from nexus.pylon.exceptions import RegexNotFoundError

from .base import (
    Md5Source,
    PreparedRequest,
)


class LibgenNewSource(Md5Source):
    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/main/{self.md5.upper()}'
            async with session.get(
                url,
                timeout=self.resolve_timeout
            ) as resp:
                downloaded_page = await resp.text()
            match_ipfs = re.search(
                'https://ipfs.io/ipfs/[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match_ipfs:
                yield PreparedRequest(method='get', url=match_ipfs.group(), ssl=self.ssl)
            match_cf = re.search(
                'https://cloudflare-ipfs.com/ipfs/[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match_cf:
                yield PreparedRequest(method='get', url=match_cf.group(), ssl=self.ssl)
            match_infura = re.search(
                'https://ipfs.infura.io/ipfs/[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match_infura:
                yield PreparedRequest(method='get', url=match_infura.group(), ssl=self.ssl)

            if not match_cf or not match_infura or not match_ipfs:
                error_log(RegexNotFoundError(url=url))


class LibraryLolSource(LibgenNewSource):
    base_url = 'http://library.lol'
    resolve_timeout = 10
    ssl = False
    timeout = 20
