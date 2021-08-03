from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [None] * len(nums)

        nums.sort()  # For detecting duplicates

        for i, num in enumerate(nums):
            if i == 0:
                subsets[i] = [[num]]

            elif i > 0 and num != nums[i - 1]:
                subsets[i] = [[num]]

                # Can get a new subset by adding `num` to each of the previous subsets
                for j in range(i):
                    for subset in subsets[j]:
                        subsets[i].append(subset + [num])

            elif i > 0 and num == nums[i - 1]:
                # `num` is a duplicate one, just need to add it to the last created
                # subsets in the previous step.
                subsets[i] = [subset + [num] for subset in subsets[i - 1]]

        result = [s for subset in subsets for s in subset]  # Flatten result
        result.append([])  # Empty set

        return result


class FailedSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        for num in range(2 ** len(nums)):
            bit_mask = format(num, "b")
            subset = []

            for i, include in enumerate(bit_mask, len(nums) - len(bit_mask)):
                if include == "1":
                    # Will create duplicate subsets as `nums` contain duplicates
                    subset.append(nums[i])

            subsets.append(subset)

        return subsets
