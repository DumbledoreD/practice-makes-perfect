from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)

        for x in sorted(arr, key=abs):
            # x is used up for pairing with x / 2
            if not counter[x]:
                continue

            if not counter[2 * x]:
                return False

            counter[x] -= 1
            counter[2 * x] -= 1

        return True
