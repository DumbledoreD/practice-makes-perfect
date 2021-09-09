from itertools import accumulate
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        return "".join(self._shift(c, s) for c, s in zip(s, self._accumulate(shifts)))

    def _shift(self, c, s):
        return chr((ord(c) - ord("a") + s) % 26 + ord("a"))

    def _accumulate(self, shifts):
        # Accumulate right to left
        return reversed(list(accumulate(reversed(shifts))))
