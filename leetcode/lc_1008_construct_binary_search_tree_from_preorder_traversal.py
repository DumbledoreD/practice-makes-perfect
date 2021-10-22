from typing import List, Optional

from .lc_tree_utils import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            cur_node = stack[-1]
            new_node = TreeNode(preorder[i])

            while stack and stack[-1].val < new_node.val:
                cur_node = stack.pop()

            if new_node.val < cur_node.val:
                cur_node.left = new_node

            else:
                cur_node.right = new_node

            stack.append(new_node)

        return root
