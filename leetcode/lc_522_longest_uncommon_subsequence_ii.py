from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        max_len = max(len(s) for s in strs)

        for l in range(max_len, 0, -1):
            subseqs = defaultdict(int)
            for s in strs:
                for subseq in combinations(s, l):
                    subseqs[subseq] += 1

            if any(count == 1 for count in subseqs.values()):
                return l

        return -1
