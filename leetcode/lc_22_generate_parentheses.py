from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return [p for p in self._gen_parenthesis("(", n - 1, n)]

    def _gen_parenthesis(self, so_far, o, c):
        if o:
            yield from self._gen_parenthesis(so_far + "(", o - 1, c)

        if c and c > o:
            yield from self._gen_parenthesis(so_far + ")", o, c - 1)

        if c == 0 and o == 0:
            yield so_far
