from typing import Optional

from .lc_tree_utils import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self._sum = 0
        self._so_far = 0
        self._traverse(root)
        return self._sum

    def _traverse(self, node):
        if node is None:
            return

        if not (node.left or node.right):
            self._sum += self._so_far * 10 + node.val
            return

        self._so_far = self._so_far * 10 + node.val
        self._traverse(node.left)
        self._traverse(node.right)
        self._so_far //= 10
