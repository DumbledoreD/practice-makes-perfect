import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_time_heap = []

        for start, end in intervals:
            if end_time_heap and end_time_heap[0] <= start:
                heapq.heapreplace(end_time_heap, end)
            else:
                heapq.heappush(end_time_heap, end)

        return len(end_time_heap)
