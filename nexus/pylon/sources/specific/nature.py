from typing import (
    AsyncIterable,
    Callable,
)

from library.logging import error_log
from nexus.pylon.sources.base import (
    DoiSource,
    PreparedRequest,
)


class NatureSource(DoiSource):
    base_url = 'https://www.nature.com'
    resolve_timeout = 10
    use_proxy = False

    async def resolve(self, error_log_func: Callable = error_log) -> AsyncIterable[PreparedRequest]:
        splitted_doi = self.doi.split("/", maxsplit=1)
        if len(splitted_doi) < 2:
            return
        url = f'{self.base_url}/articles/{splitted_doi[1].upper()}.pdf'
        yield PreparedRequest(
            method='get',
            url=url,
            timeout=self.timeout,
        )
