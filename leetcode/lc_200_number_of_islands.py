from typing import List


class Solution:
    _neighbor_offsets = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    def numIslands(self, grid: List[List[str]]) -> int:
        self._grid = grid

        count = 0
        m, n = len(self._grid), len(self._grid[0])

        for i in range(m):
            for j in range(n):
                if self._grid[i][j] == "1":
                    self._dfs(i, j)
                    count += 1

        return count

    def _dfs(self, i, j):
        stack = [(i, j)]
        self._grid[i][j] = None

        while stack:
            cur_i, cur_j = stack.pop()

            for next_i, next_j in self._get_neighbors(cur_i, cur_j):
                self._grid[next_i][next_j] = None
                stack.append((next_i, next_j))

    def _get_neighbors(self, i, j):
        m, n = len(self._grid), len(self._grid[0])

        for i_offset, j_offset in self._neighbor_offsets:
            next_i, next_j = i + i_offset, j + j_offset

            if (
                0 <= next_i < m
                and 0 <= next_j < n
                and self._grid[next_i][next_j] == "1"
            ):
                yield next_i, next_j
