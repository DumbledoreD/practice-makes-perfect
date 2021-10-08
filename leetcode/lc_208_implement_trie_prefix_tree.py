class Trie:
    def __init__(self):
        self._root = {}

    def insert(self, word: str) -> None:
        cur_node = self._root

        for c in word:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]

        cur_node["#"] = True

    def search(self, word: str) -> bool:
        cur_node = self._root

        for c in word:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]

        return "#" in cur_node

    def startsWith(self, prefix: str) -> bool:
        cur_node = self._root

        for c in prefix:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]

        return True
