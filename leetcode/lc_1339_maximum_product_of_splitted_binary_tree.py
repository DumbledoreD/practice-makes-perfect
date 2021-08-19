from typing import Optional

from .lc_tree_utils import TreeNode


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self._subtree_sum = {}
        total = self._get_subtree_sum(root)

        # max_product = 0
        # nodes = [root]

        # while nodes:
        #     cur_node = nodes.pop()

        #     if not cur_node:
        #         continue

        #     subtree_sum = self._get_subtree_sum(cur_node)
        #     max_product = max(max_product, subtree_sum * (total - subtree_sum))

        #     nodes.append(cur_node.left)
        #     nodes.append(cur_node.right)

        return max((total - s) * s for s in self._subtree_sum.values()) % (10 ** 9 + 7)

    def _get_subtree_sum(self, node):
        if not node:
            return 0

        if node in self._subtree_sum:
            return self._subtree_sum[node]

        self._subtree_sum[node] = (
            self._get_subtree_sum(node.left)
            + self._get_subtree_sum(node.right)
            + node.val
        )

        return self._subtree_sum[node]
