import math


# Unsure about the time complexity
# https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(c):
            a_sq = a * a
            b_sq = c - a_sq

            if b_sq < 0:
                return False

            b = math.isqrt(b_sq)

            if b * b == b_sq:
                return True

        # When c is 0
        return True
