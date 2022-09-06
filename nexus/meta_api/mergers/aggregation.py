from typing import List

from summa.proto import search_service_pb2


class AggregationMerger:
    def __init__(self, aggregation_collectors: List[search_service_pb2.AggregationCollectorOutput]):
        self.aggregation_collectors = aggregation_collectors

    def merge(self) -> search_service_pb2.CollectorOutput:
        return search_service_pb2.CollectorOutput(
            aggregation=self.aggregation_collectors[0]
        )
