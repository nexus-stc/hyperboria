import heapq
from typing import List

from summa.proto import search_service_pb2


class TopDocsIterator:
    def __init__(self, top_docs_collector: search_service_pb2.TopDocsCollectorOutput):
        self.top_docs_collector = top_docs_collector
        self._current = 0

    def __lt__(self, other: 'TopDocsIterator'):
        self_score = self.current().score
        other_score = other.current().score
        self_score = getattr(self_score, self_score.WhichOneof('score'))
        other_score = getattr(other_score, other_score.WhichOneof('score'))
        return self_score > other_score

    def __iter__(self):
        return self

    def __next__(self) -> search_service_pb2.ScoredDocument:
        if self.has_any():
            item = self.current()
            self._current += 1
            return item
        raise StopIteration

    def current(self):
        return self.top_docs_collector.scored_documents[self._current]

    def has_next(self) -> bool:
        return self.top_docs_collector.has_next

    def has_any(self) -> bool:
        return self._current < len(self.top_docs_collector.scored_documents)


class TopDocsMerger:
    def __init__(self, top_docs_collectors: List[search_service_pb2.TopDocsCollectorOutput]):
        self.top_docs_heap = []
        for top_docs_collector in top_docs_collectors:
            top_docs_iterator = TopDocsIterator(top_docs_collector)
            if top_docs_iterator.has_any():
                self.top_docs_heap.append(top_docs_iterator)
        heapq.heapify(self.top_docs_heap)

    def merge(self) -> search_service_pb2.CollectorOutput:
        scored_documents = []
        has_next = any([top_docs_iterator for top_docs_iterator in self.top_docs_heap])

        position = 0
        while self.top_docs_heap:
            largest_top_docs_iterator = heapq.heappop(self.top_docs_heap)
            largest_item = next(largest_top_docs_iterator)
            largest_item.position = position
            scored_documents.append(largest_item)
            position += 1
            if largest_top_docs_iterator.has_any():
                heapq.heappush(self.top_docs_heap, largest_top_docs_iterator)

        return search_service_pb2.CollectorOutput(
            top_docs=search_service_pb2.TopDocsCollectorOutput(
                has_next=has_next,
                scored_documents=scored_documents,
            )
        )
