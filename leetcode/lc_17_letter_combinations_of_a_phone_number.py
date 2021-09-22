from typing import List


class Solution:
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        return [combo for combo in self._get_combo("", digits)] if digits else []

    def _get_combo(self, so_far, rest):
        if not rest:
            yield so_far

        else:
            for c in self.mapping[rest[0]]:
                yield from self._get_combo(so_far + c, rest[1:])
