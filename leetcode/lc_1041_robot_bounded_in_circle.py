class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        self._pos = (0, 0)
        self._dir = 0  # N: 0, E: 1, S: 2, W: 3,

        for ins in instructions:
            self._go(ins)

        return self._pos == (0, 0) or self._dir != 0

    def _go(self, ins):
        if ins == "R":
            self._dir = (self._dir + 1) % 4

        elif ins == "L":
            self._dir = (self._dir - 1) % 4

        elif ins == "G":
            i, j = self._pos

            if self._dir == 0:
                self._pos = (i + 1, j)

            elif self._dir == 1:
                self._pos = (i, j + 1)

            elif self._dir == 2:
                self._pos = (i - 1, j)

            else:
                self._pos = (i, j - 1)
