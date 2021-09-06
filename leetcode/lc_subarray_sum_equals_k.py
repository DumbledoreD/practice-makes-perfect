from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        counter = defaultdict(int)

        for acc in accumulate(nums):
            if acc == k:
                count += 1

            k_comp = acc - k
            count += counter.get(k_comp, 0)

            counter[acc] += 1

        return count
