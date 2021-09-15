from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self._nums = nums
        self._nums.sort()  # For two pointer and skipping duplicates

        summands = []

        for i, x in enumerate(self._nums):
            # Skip duplicates
            if i > 0 and self._nums[i] == self._nums[i - 1]:
                continue

            for y, z in self._two_pointer_two_sum(i + 1, 0 - x):
                summands.append((x, y, z))

        return summands

    def _two_pointer_two_sum(self, l, k):
        r = len(self._nums) - 1

        while l < r:
            two_sum = self._nums[l] + self._nums[r]

            if two_sum < k:
                l += 1

            elif two_sum > k:
                r -= 1

            else:
                yield self._nums[l], self._nums[r]

                l += 1
                r -= 1

                # Skip duplicates only when summands are found
                # Consider [-1, -1] and k is -2
                while l < r and self._nums[l] == self._nums[l - 1]:
                    l += 1

                while l < r and self._nums[r] == self._nums[r + 1]:
                    r -= 1


class SlowSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self._nums = nums
        self._preprocess_nums()

        results = set()
        seen = set()

        for i, x in enumerate(self._nums):
            if x in seen:
                continue
            seen.add(x)

            for y, z in self._two_sum(0 - x, i):
                results.add(tuple(sorted([x, y, z])))

        return results

    def _preprocess_nums(self):
        self._num_to_index = defaultdict(list)

        for i, num in enumerate(self._nums):
            self._num_to_index[num].append(i)

    def _two_sum(self, k, skipped_index):
        for y_i, y in enumerate(self._nums):
            if y_i == skipped_index:
                continue

            z = self._get_num(k - y, y_i, skipped_index)

            if z is not None:
                yield y, z

    def _get_num(self, num, *skipped_indices):
        num_i = next(
            (i for i in self._num_to_index[num] if i not in skipped_indices), None
        )
        return None if num_i is None else num
