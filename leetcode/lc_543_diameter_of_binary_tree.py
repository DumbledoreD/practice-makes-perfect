from typing import Optional

from .lc_tree_utils import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._diameter = 0

        self._longest_path(root)

        return self._diameter

    def _longest_path(self, node):
        if not node:
            return -1, -1

        left = max(self._longest_path(node.left)) + 1
        right = max(self._longest_path(node.right)) + 1

        self._diameter = max(self._diameter, left + right)

        return left, right
