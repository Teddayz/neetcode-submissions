class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        # Inserts all the words into the Trie
        for i in range(len(words)):
            curr = self.root
            for char in words[i]:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True
            curr.index = i
        res = []
        m = len(board)
        n = len(board[0])
        def check(row: int, col: int, node: TrieNode, res: List[str]) -> None:
            curr = node
            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] == "#":
                return
            char = board[row][col]
            
            if char not in node.children:
                board[row][col] = char
                return
            curr = node.children[char]
            if curr.endOfWord:
                if curr.index != -1:
                    res.append(words[curr.index])
                curr.index = -1
            
            board[row][col] = "#"
            check(row - 1, col, curr, res)
            check(row + 1, col, curr, res)
            check(row, col - 1, curr, res)
            check(row, col + 1, curr, res)
            board[row][col] = char

        for row in range(m):
            for col in range(n):
                if board[row][col] not in self.root.children:
                    continue
                check(row, col, self.root, res)
        
        return res

