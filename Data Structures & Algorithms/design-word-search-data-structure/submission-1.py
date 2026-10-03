class TrieNode:

    def __init__(self, children=None):
        if children:
            self.children = children
        else:
            self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        return
        

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)
        

    def search_helper(self, word, node) -> bool:
        curr = node
        for i in range(len(word)):
            if word[i] == '.':
                for (key, node) in curr.children.items():
                    if self.search_helper(word[i+1:], node) == True:
                        return True

            if word[i] not in curr.children:
                return False

            curr = curr.children[word[i]]
        return curr.endOfWord
        
