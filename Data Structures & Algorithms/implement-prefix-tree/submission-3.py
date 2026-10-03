class PrefixTree:

    def __init__(self):
        self.root = self.TrieNode()    

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                node = self.TrieNode()
                curr.children[char] = node
            curr = curr.children[char]
        curr.endOfWord = True
        return

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr != None
        
    class TrieNode:

        def __init__(self) -> None:
            self.children = {}
            self.endOfWord = False

        
        