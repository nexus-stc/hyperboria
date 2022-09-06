import random
import sys
from typing import List

from summa.proto import search_service_pb2


class ReservoirSamplingMerger:
    def __init__(self, reservoir_sampling_collectors: List[search_service_pb2.ReservoirSamplingCollectorOutput]):
        self.reservoir_sampling_collectors = reservoir_sampling_collectors

    def merge(self) -> search_service_pb2.ReservoirSamplingCollectorOutput:
        random_documents = []
        for reservoir_sampling_collector in self.reservoir_sampling_collectors:
            random_documents += reservoir_sampling_collector.random_documents
        random.shuffle(random_documents)
        return search_service_pb2.CollectorOutput(
            reservoir_sampling=search_service_pb2.ReservoirSamplingCollectorOutput(
                random_documents=random_documents
            )
        )
