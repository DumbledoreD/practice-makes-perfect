from itertools import accumulate
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._acc_nums = list(accumulate(nums))
        self._acc_nums.append(0)

    def sumRange(self, left: int, right: int) -> int:
        return self._acc_nums[right] - self._acc_nums[left - 1]
