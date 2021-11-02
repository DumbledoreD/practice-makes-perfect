from typing import List


class Solution:
    _dir_offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self._grid = grid
        # Add 1 to _empty_count for the starting block
        self._start, self._end, self._empty_count = None, None, 1
        self._path_count = 0

        self._scan_grid()
        self._dfs(*self._start)

        return self._path_count

    def _scan_grid(self):
        for i in range(len(self._grid)):
            for j in range(len(self._grid[0])):
                if self._grid[i][j] == 0:
                    self._empty_count += 1

                elif self._grid[i][j] == 1:
                    self._start = (i, j)

                elif self._grid[i][j] == 2:
                    self._end = (i, j)

    def _dfs(self, i, j):
        if (i, j) == self._end and self._empty_count == 0:
            self._path_count += 1
            return

        self._grid[i][j] = 3
        self._empty_count -= 1

        for next_i, next_j in self._next_pos(i, j):
            self._dfs(next_i, next_j)

        self._grid[i][j] = 0
        self._empty_count += 1

    def _next_pos(self, i, j):
        for i_p, j_p in self._dir_offset:
            next_i = i + i_p
            next_j = j + j_p
            is_valid_pos = 0 <= next_i < len(self._grid) and 0 <= next_j < len(
                self._grid[0]
            )

            if is_valid_pos and self._grid[next_i][next_j] == 0:
                yield next_i, next_j

            elif (
                is_valid_pos
                and self._grid[next_i][next_j] == 2
                and self._empty_count == 0
            ):
                yield next_i, next_j
