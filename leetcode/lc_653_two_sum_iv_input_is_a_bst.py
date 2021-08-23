from typing import Optional

from .lc_tree_utils import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self._in_order = []
        self._in_order_traversal(root)
        return self._two_pointer(k)

    def _in_order_traversal(self, node):
        if not node:
            return

        self._in_order_traversal(node.left)
        self._in_order.append(node.val)
        self._in_order_traversal(node.right)

    def _two_pointer(self, k):
        l = 0
        r = len(self._in_order) - 1

        while l < r:
            s = self._in_order[l] + self._in_order[r]

            if s == k:
                return True

            if s < k:
                l += 1

            else:
                r -= 1

        return False
