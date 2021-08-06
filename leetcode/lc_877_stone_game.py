from functools import lru_cache
from typing import List


# Turn the failed solution into a dp
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self._piles = piles
        return self._dp(0, len(self._piles) - 1) > 0

    @lru_cache(None)
    def _dp(self, i, j):
        """dp(i, j) is the max diff between p0's and p1's score with piles[i:j+1]"""

        if i > j:
            return 0

        player = (j + 1 - i - len(self._piles)) % 2

        if player == 0:
            return max(
                self._piles[i] + self._dp(i + 1, j),  # p0 takes left
                self._piles[j] + self._dp(i, j - 1),  # p0 takes right
            )
        else:
            return min(
                -self._piles[i] + self._dp(i + 1, j),  # p1 takes left
                -self._piles[j] + self._dp(i, j - 1),  # p2 takes right
            )


# Can't find a test case where the first player lose?
# Always True when len(piles) is even
class CheatSolution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


# ERROR: Time Limit Exceeded, O(2^n)
class FailedSolution:
    def stoneGame(self, piles: List[int]) -> bool:
        self._piles = piles
        return self._is_winnable(0, len(piles) - 1, 0, 0, 0)

    def _is_winnable(self, i, j, p0_score, p1_score, cur_player):
        if i == j:
            p0_score += (cur_player == 0) * self._piles[i]
            p1_score += (cur_player == 1) * self._piles[i]
            return p0_score > p1_score

        op1_result = self._is_winnable(
            i + 1,  # Take left
            j,
            p0_score + (cur_player == 0) * self._piles[i],
            p1_score + (cur_player == 1) * self._piles[i],
            (cur_player + 1) % 2,
        )

        op2_result = self._is_winnable(
            i,
            j - 1,  # Take right
            p0_score + (cur_player == 0) * self._piles[j],
            p1_score + (cur_player == 1) * self._piles[j],
            (cur_player + 1) % 2,
        )

        return (
            op1_result or op2_result if cur_player == 0 else op1_result and op2_result
        )
