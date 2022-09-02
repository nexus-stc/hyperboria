from typing import List

from summa.proto import search_service_pb2


class CountMerger:
    def __init__(self, count_collectors: List[search_service_pb2.CountCollectorOutput]):
        self.count_collectors = count_collectors

    def merge(self) -> search_service_pb2.CollectorOutput:
        return search_service_pb2.CollectorOutput(
            count=search_service_pb2.CountCollectorOutput(
                count=sum([count_collector.count for count_collector in self.count_collectors])
            )
        )

