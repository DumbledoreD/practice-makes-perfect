from collections import deque
from typing import List

from .lc_tree_utils import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        self._target_sum = target_sum
        self._child_to_parent = {}

        paths = []

        for leaf_node in self._traverse(0, root):
            path = self._build_path(leaf_node)
            paths.append(path)

        return paths

    def _traverse(self, so_far, cur_node):
        if cur_node is None:
            return

        cur_val = so_far + cur_node.val

        # Reach leaf
        if cur_node.left is None and cur_node.right is None:
            if cur_val == self._target_sum:
                yield cur_node

        else:
            self._child_to_parent[cur_node.left] = cur_node
            yield from self._traverse(cur_val, cur_node.left)

            self._child_to_parent[cur_node.right] = cur_node
            yield from self._traverse(cur_val, cur_node.right)

    def _build_path(self, leaf_node):
        path = deque()
        cur_node = leaf_node

        while cur_node:
            path.appendleft(cur_node.val)
            cur_node = self._child_to_parent.get(cur_node)

        return list(path)
