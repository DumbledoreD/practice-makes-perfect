class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode(val={}, left={}, right={})".format(
            self.val,
            self.left and self.left.val,
            self.right and self.right.val,
        )


class BinaryTreeBuilder:
    node_class = TreeNode

    def build(self, tree_list):
        if not tree_list:
            return None

        nodes = [None if val is None else self.node_class(val) for val in tree_list]
        children = nodes[::-1]
        root = children.pop()

        for node in nodes:
            if node:
                if children:
                    node.left = children.pop()
                if children:
                    node.right = children.pop()

        return root
