from itertools import accumulate
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_acc = 0

        for i, acc in enumerate(accumulate(nums)):
            max_sum = max(max_sum, acc - min_acc)
            min_acc = min(min_acc, acc)

        return max_sum
