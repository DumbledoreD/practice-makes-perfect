from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self._nums1, self._nums2 = nums1, nums2
        self._build_next_greater_dict()
        return [self._next_greater_dict.get(num, -1) for num in self._nums1]

    def _build_next_greater_dict(self):
        self._next_greater_dict = {}

        stack = []

        for num in self._nums2:
            while stack and num > stack[-1]:
                self._next_greater_dict[stack.pop()] = num

            stack.append(num)
