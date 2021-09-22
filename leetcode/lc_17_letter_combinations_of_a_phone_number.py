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

    def _get_combo(self, sofar, rest):
        if not rest:
            yield sofar

        else:
            for c in self.mapping[rest[0]]:
                yield from self._get_combo(sofar + c, rest[1:])
