class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        expect = 1

        for node in preorder.split(","):
            # Can only be 0 after all nodes are visited
            if expect == 0:
                return False

            # Expect 2 children if current node has value, 2 - 1 = 1
            expect += -1 if node == "#" else 1

        return expect == 0
