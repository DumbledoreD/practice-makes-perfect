from typing import Optional

from .lc_tree_utils import TreeNode


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        child_to_parent = {}
        nodes = [root]
        found = 0

        while found == 0 and nodes:

            next_nodes = []

            for node in nodes:
                if node.val == x or node.val == y:
                    found += 1

                if node.left:
                    child_to_parent[node.left.val] = node.val
                    next_nodes.append(node.left)

                if node.right:
                    child_to_parent[node.right.val] = node.val
                    next_nodes.append(node.right)

                nodes = next_nodes

        return found == 2 and child_to_parent[x] != child_to_parent[y]
