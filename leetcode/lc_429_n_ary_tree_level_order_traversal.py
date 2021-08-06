from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        result = []

        if root is None:
            return result

        cur_level = [root]

        while cur_level:
            cur_level_values = []
            next_level = []

            for node in cur_level:
                cur_level_values.append(node.val)
                next_level.extend(node.children)

            result.append(cur_level_values)
            cur_level = next_level

        return result
