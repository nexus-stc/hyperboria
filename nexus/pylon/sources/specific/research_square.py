import re
from typing import AsyncIterable

from nexus.pylon.exceptions import RegexNotFoundError

from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class ResearchSquareSource(DoiSource):
    base_url = 'https://dx.doi.org'

    async def resolve(self) -> AsyncIterable[PreparedRequest]:
        async with self.get_resolve_session() as session:
            url = f'{self.base_url}/{self.doi}'
            async with session.get(
                url,
                timeout=self.resolve_timeout
            ) as resp:
                download_page = await resp.text()
            match = re.search(
                r'\"(https://www\.researchsquare\.com/article/[^\"]+\.pdf)\"',
                download_page,
                re.IGNORECASE,
            )
            if not match:
                raise RegexNotFoundError(url=url)
            yield PreparedRequest(method='get', url=match.group(1))
