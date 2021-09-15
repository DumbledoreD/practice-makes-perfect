class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = set()
        open_paren = []

        for i, c in enumerate(s):
            if c == "(":
                open_paren.append(i)

            elif c == ")":
                if open_paren:
                    open_paren.pop()
                else:
                    invalid.add(i)

        invalid.update(open_paren)

        return "".join(c for i, c in enumerate(s) if i not in invalid)
