from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            num_comp = target - num
            if num_comp in seen:
                return [i, seen[num_comp]]
            else:
                seen[num] = i

        return None
