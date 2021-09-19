from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = min(strs, key=len)

        for s in strs:
            if not (longest := self._common_prefix(longest, s)):
                break

        return longest

    def _common_prefix(self, a, b):
        for i, (a_i, b_i) in enumerate(zip(a, b)):
            if a_i != b_i:
                return a[:i]

        return min(a, b, key=len)
