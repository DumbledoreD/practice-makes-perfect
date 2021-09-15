from operator import eq, gt, lt
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_count, count = 0, 0
        prev_sign = eq

        for i in range(1, len(arr)):
            cur_sign = self._comp(arr[i - 1], arr[i])

            if cur_sign == eq:
                count = 0

            elif cur_sign == prev_sign:
                count = 1

            else:
                count += 1

            max_count = max(max_count, count)
            prev_sign = cur_sign

        return max_count + 1

    def _comp(self, a, b):
        if lt(a, b):
            return lt

        if gt(a, b):
            return gt

        return eq
