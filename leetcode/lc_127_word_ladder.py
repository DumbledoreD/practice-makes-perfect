from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        self._build_adj_list(word_list)
        return self._bfs(begin_word, end_word)

    def _build_adj_list(self, word_list):
        self._adj_list = defaultdict(list)

        for word in word_list:
            for mask in self._get_mask(word):
                self._adj_list[mask].append(word)

    def _get_mask(self, word):
        chars = list(word)

        for i, c in enumerate(chars):
            chars[i] = "*"
            yield "".join(chars)
            chars[i] = c

    def _bfs(self, begin_word, end_word):
        seen = set()
        queue = deque()

        seen.add(begin_word)
        queue.append((begin_word, 1))

        while queue:
            cur_word, steps = queue.popleft()
            steps += 1

            for next_word in self._get_next_word(cur_word, seen):
                if next_word == end_word:
                    return steps

                seen.add(next_word)
                queue.append((next_word, steps))

        return 0

    def _get_next_word(self, cur_word, seen):
        for mask in self._get_mask(cur_word):
            for word in self._adj_list.get(mask, []):
                if word not in seen:
                    yield word
