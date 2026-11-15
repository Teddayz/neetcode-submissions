class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word, 0)

    def _search(self, node, word, i):
        while i < len(word):
            char = word[i]
            if char == ".":
                for child in node.children.values():
                    if self._search(child, word, i + 1):
                        return True
                return False
            if char not in node.children:
                return False
            node = node.children[char]
            i += 1
        return node.endOfWord