class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letter_stack = [c for c in s if c.isalpha()]
        return "".join(letter_stack.pop() if c.isalpha() else c for c in s)
