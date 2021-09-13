from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        self._n = n

        self._mines_set = {tuple(mine) for mine in mines}
        self._dp = [[0] * self._n for _ in range(n)]
        self._accumulate_left_right()
        self._accumulate_up_down()

        return self._max

    # Has to be left_right, left_up doesn't work, consider [[0 , 1], [1, 1]]
    # dp[1][1] should be 2. If I do left_up, dp[1][1] is 1.
    def _accumulate_left_right(self):
        for i in range(self._n):
            size = 0
            for j in range(self._n):
                size = 0 if (i, j) in self._mines_set else size + 1
                self._dp[i][j] = size

            size = 0
            for j in range(self._n - 1, -1, -1):
                size = 0 if (i, j) in self._mines_set else size + 1
                self._dp[i][j] = min(self._dp[i][j], size)

    def _accumulate_up_down(self):
        self._max = 0

        for j in range(self._n):
            size = 0
            for i in range(self._n):
                size = 0 if (i, j) in self._mines_set else size + 1
                self._dp[i][j] = min(self._dp[i][j], size)

            size = 0
            for i in range(self._n - 1, -1, -1):
                size = 0 if (i, j) in self._mines_set else size + 1
                self._dp[i][j] = min(self._dp[i][j], size)

                self._max = max(self._max, self._dp[i][j])
