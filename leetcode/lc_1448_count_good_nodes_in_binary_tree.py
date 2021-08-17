from .lc_tree_utils import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        nodes = [(-float("inf"), root)]

        while nodes:
            max_so_far, cur_node = nodes.pop()

            if not cur_node:
                continue

            if cur_node.val >= max_so_far:
                count += 1

            max_so_far = max(max_so_far, cur_node.val)

            nodes.append((max_so_far, cur_node.left))
            nodes.append((max_so_far, cur_node.right))

        return count
