import re
from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.exceptions import RegexNotFoundError

from .base import (
    Md5Source,
    PreparedRequest,
)


class LibgenNewSource(Md5Source):
    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/main/{self.md5.upper()}'
            async with PreparedRequest(
                method='get',
                url=url,
                timeout=self.resolve_timeout
            ).execute_with(session) as resp:
                downloaded_page = await resp.text()
            match_ipfs = re.search(
                'https://ipfs.io/ipfs/[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match_ipfs:
                yield PreparedRequest(method='get', url=match_ipfs.group(), ssl=self.ssl, timeout=self.timeout)
            match_cf = re.search(
                'https://cloudflare-ipfs.com/ipfs/[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match_cf:
                yield PreparedRequest(method='get', url=match_cf.group(), ssl=self.ssl, timeout=self.timeout)
            match_infura = re.search(
                'https://ipfs.infura.io/ipfs/[A-Za-z0-9]+',
                downloaded_page,
                re.IGNORECASE,
            )
            if match_infura:
                yield PreparedRequest(method='get', url=match_infura.group(), ssl=self.ssl, timeout=self.timeout)

            if not match_cf or not match_infura or not match_ipfs:
                error_log_func(RegexNotFoundError(url=url))


class LibraryLolSource(LibgenNewSource):
    base_url = 'http://library.lol'
    resolve_timeout = 20
    ssl = False
    timeout = 120
