from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)

        return min(
            counter.get("b", 0),
            counter.get("a", 0),
            counter.get("l", 0) // 2,
            counter.get("o", 0) // 2,
            counter.get("n", 0),
        )
