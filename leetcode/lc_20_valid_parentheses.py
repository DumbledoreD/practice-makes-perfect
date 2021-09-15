class Solution:
    CLOSE_TO_OPEN = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in self.CLOSE_TO_OPEN:
                if not (stack and stack.pop() == self.CLOSE_TO_OPEN[p]):
                    return False
            else:
                stack.append(p)

        return not stack
