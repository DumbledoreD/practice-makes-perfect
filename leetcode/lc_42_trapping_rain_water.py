from itertools import accumulate
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = list(accumulate(height, func=max))
        right_max = list(accumulate(reversed(height), func=max))[::-1]

        trapped = 0

        for i, h in enumerate(height):
            trapped += min(left_max[i], right_max[i]) - h

        return trapped
