from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not (nums1 and nums2):
            return self._median(nums1 or nums2)

        if nums1[-1] <= nums2[0]:
            return self._median_of_non_overlaps(nums1, nums2)

        if nums2[-1] <= nums1[0]:
            return self._median_of_non_overlaps(nums2, nums1)

        return self._median_of_overlaps(nums1, nums2)

    def _median(self, nums):
        div, mod = divmod(len(nums), 2)

        if mod:
            return nums[div]

        return (nums[div - 1] + nums[div]) / 2

    def _median_of_non_overlaps(self, lesser, greater):
        div, mod = divmod(len(lesser) + len(greater), 2)

        if mod:
            return self._get_i_th_elment_from_2_lists(lesser, greater, div)

        return (
            self._get_i_th_elment_from_2_lists(lesser, greater, div - 1)
            + self._get_i_th_elment_from_2_lists(lesser, greater, div)
        ) / 2

    def _get_i_th_elment_from_2_lists(self, lesser, greater, i):
        if i < len(lesser):
            return lesser[i]

        return greater[i - len(lesser)]

    def _median_of_overlaps(self, nums1, nums2):
        left_length, mod = divmod(len(nums1) + len(nums2), 2)

        left_length += mod  # In case of odd, put the median in the left partition

        shorter, longer = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        l, r = 0, len(shorter)

        while l <= r:
            p_shorter = (l + r) // 2
            p_longer = left_length - p_shorter

            # [... shorter_l | shorter_r ...]
            shorter_l = self._get_i_th_elment_from_1_list(shorter, p_shorter - 1)
            shorter_r = self._get_i_th_elment_from_1_list(shorter, p_shorter)

            # [... longer_l | longer_r ...]
            longer_l = self._get_i_th_elment_from_1_list(longer, p_longer - 1)
            longer_r = self._get_i_th_elment_from_1_list(longer, p_longer)

            if shorter_l <= longer_r and longer_l <= shorter_r:
                return (
                    max(shorter_l, longer_l)
                    if mod
                    else (max(shorter_l, longer_l) + min(shorter_r, longer_r)) / 2
                )

            elif shorter_l > longer_r:
                r = p_shorter - 1

            else:
                l = p_shorter + 1

        raise Exception("Failed binary search")

    def _get_i_th_elment_from_1_list(self, nums, i):
        if i < 0:
            return -float("inf")

        if i >= len(nums):
            return float("inf")

        return nums[i]
