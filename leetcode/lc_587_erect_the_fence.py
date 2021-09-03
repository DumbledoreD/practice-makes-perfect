# Ref: http://www.algorithmist.com/index.php/Monotone_Chain_Convex_Hull.py
# Computes the convex hull of a set of 2D points.
from typing import List


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 3:
            return points

        points.sort()

        hull = []

        for p in points:
            while len(hull) >= 2 and not self._is_convex(hull[-2], hull[-1], p):
                hull.pop()
            hull.append(tuple(p))

        lower_hull_length = len(hull)

        for p in reversed(points):
            while len(hull) >= lower_hull_length + 2 and not self._is_convex(
                hull[-2], hull[-1], p
            ):
                hull.pop()
            hull.append(tuple(p))

        # Need to take set, consider the case where all points are on the same line
        return list(set(p for p in hull))

    def _is_convex(self, o, a, b):
        cross_product = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        return cross_product >= 0
