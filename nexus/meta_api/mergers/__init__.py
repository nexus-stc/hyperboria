from .aggregation import AggregationMerger
from .count import CountMerger
from .reservoir_sampling import ReservoirSamplingMerger
from .top_docs import TopDocsMerger

__all__ = ['AggregationMerger', 'CountMerger', 'TopDocsMerger', 'ReservoirSamplingMerger']
