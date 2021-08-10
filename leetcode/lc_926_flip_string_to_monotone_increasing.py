from functools import lru_cache
from itertools import accumulate


class IterativeSolution:
    def minFlipsMonoIncr(self, s: str) -> int:
        min_flips = 0
        ones = 0

        for i in s:
            if i == "1":
                ones += 1

            else:
                min_flips = min(
                    min_flips + 1,  # Flip the current 0
                    ones,  # Flip all previous 1s
                )

        return min_flips


class RecursiveSolution:
    def minFlipsMonoIncr(self, s: str) -> int:
        self._s = s
        self._ones_count = list(accumulate(map(int, s)))
        return self._dp(len(s) - 1)

    @lru_cache(maxsize=None)
    def _dp(self, i):
        """Min number of flips to get monotone increasing s[:i + 1]"""
        if i == 0:
            return 0

        if self._s[i] == "1":
            return self._dp(i - 1)

        else:
            return min(
                self._dp(i - 1) + 1,  # Flip the current 0
                self._ones_count[i],  # Flip all previous 1s
            )
