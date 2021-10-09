from typing import List


class Solution:
    _OFFSETS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    def exist(self, board: List[List[str]], word: str) -> bool:
        self._board = board
        self._word = word

        self._n, self._m = len(self._board), len(self._board[0])

        for i in range(self._n):
            for j in range(self._m):
                if self._board[i][j] == self._word[0]:
                    self._seen = set()
                    if self._dfs(i, j, 0):
                        return True

        return False

    def _dfs(self, i, j, k):
        next_k = k + 1

        if next_k == len(self._word):
            return True

        self._seen.add((i, j))

        for next_i, next_j in self._get_next_node(i, j, next_k):
            if self._dfs(next_i, next_j, next_k):
                return True

        self._seen.remove((i, j))

        return False

    def _get_next_node(self, i, j, next_k):
        for i_offset, j_offset in self._OFFSETS:
            next_i = i + i_offset
            next_j = j + j_offset

            if (
                (0 <= next_i < self._n)
                and (0 <= next_j < self._m)
                and (next_i, next_j) not in self._seen
                and self._board[next_i][next_j] == self._word[next_k]
            ):
                yield (next_i, next_j)
