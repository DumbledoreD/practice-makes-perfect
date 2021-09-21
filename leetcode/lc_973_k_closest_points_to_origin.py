import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x * x + y * y, (x, y)) for x, y in points]
        heapq.heapify(points)
        return [heapq.heappop(points)[1] for i in range(k)]
