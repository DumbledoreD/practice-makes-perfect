from functools import lru_cache
from typing import List


class Solution:
    def jobScheduling(
        self, start_time: List[int], end_time: List[int], profit: List[int]
    ) -> int:
        self._jobs = sorted(zip(start_time, end_time, profit))
        return self._max_profit_from_i(0)

    @lru_cache(maxsize=None)
    def _max_profit_from_i(self, i):
        if i == len(self._jobs):
            return 0

        _, end_time_i, profit_i = self._jobs[i]

        for j in range(i + 1, len(self._jobs)):
            start_time_j, _, _ = self._jobs[j]
            if start_time_j >= end_time_i:
                break
        else:
            j = len(self._jobs)

        return max(
            profit_i + self._max_profit_from_i(j),  # Take job i
            self._max_profit_from_i(i + 1),  # Skip job i
        )
