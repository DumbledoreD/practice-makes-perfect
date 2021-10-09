from typing import List


class Solution:
    _OFFSETS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    _EOW = "$"
    _VISITED = "#"

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self._board = board
        self._words = words

        self._build_trie()

        self._n, self._m = len(self._board), len(self._board[0])

        self._words_found = []

        for i in range(self._n):
            for j in range(self._m):
                if self._board[i][j] in self._trie:
                    self._dfs(i, j, self._trie)

        return self._words_found

    def _build_trie(self):
        self._trie = {}

        for word in self._words:
            cur_node = self._trie

            for c in word:
                if c not in cur_node:
                    cur_node[c] = {}
                cur_node = cur_node[c]

            cur_node[self._EOW] = word

    def _dfs(self, i, j, trie_node):
        next_trie_node = trie_node[self._board[i][j]]

        if self._EOW in next_trie_node:
            self._words_found.append(next_trie_node.pop(self._EOW))

        # Prune leaf nodes
        if not next_trie_node:
            trie_node.pop(self._board[i][j])
            return

        # Mark visited
        c = self._board[i][j]
        self._board[i][j] = self._VISITED

        for next_i, next_j in self._get_next_node(i, j, next_trie_node):
            self._dfs(next_i, next_j, next_trie_node)

        # Restore on post-order
        self._board[i][j] = c

    def _get_next_node(self, i, j, next_trie_node):
        for i_offset, j_offset in self._OFFSETS:
            next_i = i + i_offset
            next_j = j + j_offset

            if (
                (0 <= next_i < self._n)
                and (0 <= next_j < self._m)
                and self._board[next_i][next_j] in next_trie_node
            ):
                yield (next_i, next_j)
