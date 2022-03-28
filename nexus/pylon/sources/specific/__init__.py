from typing import Iterable

from ..base import DoiSource
from .biorxiv import BiorxivSource
from .lancet import LancetSource
from .nature import NatureSource
from .nejm import NejmSource
from .pnas import PnasSource
from .research_square import ResearchSquareSource

paper_sources = {
    '10.1016': [LancetSource],
    '10.1038': [NatureSource],
    '10.1056': [NejmSource],
    '10.1073': [PnasSource],
    '10.1101': [BiorxivSource],
    '10.21203': [ResearchSquareSource],
}


def get_specific_sources_for_doi(doi: str, **kwargs) -> Iterable[DoiSource]:
    source_clses = paper_sources.get(doi.split('/')[0], [])
    source_clses = list(map(lambda cls: cls(doi, **kwargs), source_clses))
    return source_clses
