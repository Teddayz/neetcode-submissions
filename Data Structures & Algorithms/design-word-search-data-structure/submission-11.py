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
        return self.search_from_node(self.root, word, 0)

    def search_from_node(self, node, word, index):
        while index < len(word):
            if word[index] == ".":
                for key, trieNode in node.children.items():
                    if self.search_from_node(trieNode, word, index + 1):
                        return True
                return False
            elif word[index] not in node.children:
                return False
            else:
                node = node.children[word[index]]
                index += 1
        return node.endOfWord



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)