class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        longest = 0
        unique_from = 0

        for i, c in enumerate(s):
            # Last seen could be stale. Consider "tmmtabc".
            if c in last_seen and last_seen[c] + 1 > unique_from:
                unique_from = last_seen[c] + 1

            else:
                longest = max(longest, i - unique_from + 1)

            last_seen[c] = i

        return longest
