from typing import List


# Requirements: In place and use constant space
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        self._nums = nums

        for i in range(len(self._nums) - 2, -1, -1):
            if self._nums[i] < self._nums[i + 1]:
                j = self._smallest_greater_than_i(i)
                self._nums[i], self._nums[j] = self._nums[j], self._nums[i]
                self._reverse_from_i(i + 1)
                break

        else:
            self._reverse_from_i(0)

    def _smallest_greater_than_i(self, i):
        j = i

        while j + 1 < len(self._nums) and self._nums[j + 1] > self._nums[i]:
            j += 1

        return j

    def _reverse_from_i(self, i):
        l, r = i, len(self._nums) - 1

        while l < r:
            self._nums[l], self._nums[r] = self._nums[r], self._nums[l]
            l += 1
            r -= 1
