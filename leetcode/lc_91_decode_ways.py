from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        self._s = s
        self._count = 0
        return self._backtrack(0)

    @lru_cache(maxsize=None)  # Overlapping subproblems
    def _backtrack(self, cur_index):
        if cur_index == len(self._s):
            return 1

        elif self._s[cur_index] == "0":
            return 0

        else:
            count = self._backtrack(cur_index + 1)  # Take one digit

            if 10 <= int(self._s[cur_index : cur_index + 2]) <= 26:
                count += self._backtrack(cur_index + 2)  # Take two digits

            return count
