import heapq
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        heapq.heapify(intervals)

        start, end = heapq.heappop(intervals)

        while intervals:
            next_start, next_end = heapq.heappop(intervals)

            #  Overlap
            if next_start <= end:
                end = max(end, next_end)

            # Non-overlap
            else:
                merged.append([start, end])
                start, end = next_start, next_end

        merged.append([start, end])

        return merged
