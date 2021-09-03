from functools import lru_cache
from typing import List, Optional

from .lc_tree_utils import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self._gen_tree_from_range(1, n)

    @lru_cache(maxsize=None)
    def _gen_tree_from_range(self, start: int, end: int) -> TreeNode:
        if end < start:
            return [None]

        elif start == end:
            return [TreeNode(start, None, None)]

        trees = []

        for root in range(start, end + 1):
            for left in self._gen_tree_from_range(start, root - 1):
                for right in self._gen_tree_from_range(root + 1, end):
                    trees.append(TreeNode(root, left, right))

        return trees


# Can't use cache with generator
class SlowSolution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return list(self._gen_tree_from_range(1, n))

    def _gen_tree_from_range(self, start: int, end: int) -> TreeNode:
        if end < start:
            yield None

        elif start == end:
            yield TreeNode(start, None, None)

        else:
            for root in range(start, end + 1):
                for left in self._gen_tree_from_range(start, root - 1):
                    for right in self._gen_tree_from_range(root + 1, end):
                        yield TreeNode(root, left, right)
