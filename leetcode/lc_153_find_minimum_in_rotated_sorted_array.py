from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_num = nums[0]

        while r > l:
            m = (l + r) // 2

            min_num = min(min_num, nums[m], nums[l], nums[r])

            if nums[m] > nums[r]:
                l = m + 1

            else:
                r = m - 1

        return min_num
