from collections import Counter
from typing import List


# Account for the follow ups:
# 1. len(nums1) < len(nums2)
# 2. Can't load all elements of num2 into memory
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        intersection = Counter()

        for num in nums2:
            intersection[num] = min(intersection[num] + 1, nums1_counter[num])

        return intersection.elements()
