from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self._s, self._t = s, t
        count = self._count_t_j_from_s_i(0, 0)
        self._count_t_j_from_s_i.cache_clear()
        return count

    @lru_cache(maxsize=None)
    def _count_t_j_from_s_i(self, i, j):
        """Count num of t[j:] in s[i:]"""
        if len(self._t) - j > len(self._s) - i:
            return 0

        if j == len(self._t):
            return 1

        count = 0

        for k in range(i, len(self._s)):
            if self._s[k] == self._t[j]:
                count += self._count_t_j_from_s_i(k + 1, j + 1)

        return count
