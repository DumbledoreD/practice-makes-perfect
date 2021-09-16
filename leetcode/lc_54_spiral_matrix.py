from typing import List


class SpiralIterator:
    _steps = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
        (-1, 0),  # up
    ]

    def __init__(self, matrix):
        self._matrix = matrix

    def __iter__(self):
        self._i_lb, self._i_ub = 0, len(self._matrix) - 1
        self._j_lb, self._j_ub = 0, len(self._matrix[0]) - 1

        self._i, self._j = 0, -1
        self._dir = 0  # 0: right, 1: down, 2: left, 3: up
        return self

    def __next__(self):
        i, j = self._step()

        if not self._validate(i, j):
            self._change_dir()
            i, j = self._step()

            if not self._validate(i, j):
                raise StopIteration()

        self._i, self._j = i, j
        return self._matrix[i][j]

    def _step(self):
        i_step, j_step = self._steps[self._dir]
        return self._i + i_step, self._j + j_step

    def _validate(self, i, j):
        return (
            (self._dir == 0 and j <= self._j_ub)
            or (self._dir == 1 and i <= self._i_ub)
            or (self._dir == 2 and j >= self._j_lb)
            or (self._dir == 3 and i >= self._i_lb)
        )

    def _change_dir(self):
        if self._dir == 0:
            self._i_lb += 1

        elif self._dir == 1:
            self._j_ub -= 1

        elif self._dir == 2:
            self._i_ub -= 1

        elif self._dir == 3:
            self._j_lb += 1

        self._dir = (self._dir + 1) % 4


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return list(SpiralIterator(matrix))
