from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self._nums = nums
        self._seen = set()
        max_length = 0

        for k, num in enumerate(self._nums):
            if num not in self._seen:
                max_length = max(max_length, self._get_s_k_length(k))

        return max_length

    def _get_s_k_length(self, k):
        s_k = set()
        num = self._nums[k]

        while num not in s_k:
            s_k.add(num)
            num = self._nums[num]

        self._seen |= s_k

        return len(s_k)
