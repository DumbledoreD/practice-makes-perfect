from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            # Only consists of lower-case English letters.
            # Use count sort as an optimization.
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            anagrams[tuple(count)].append(s)

        return anagrams.values()
