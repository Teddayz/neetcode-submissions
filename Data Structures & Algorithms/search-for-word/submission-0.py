class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ans = False
        def dfs(remaining_word: str, row: int, col: int) -> bool:
            # Go and check the neighbours and if remaining_word == None, we found a word
            if not remaining_word:
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != remaining_word[0] or board[row][col] == "#":
                return False
    
            temp = board[row][col]
            board[row][col] = "#"
            result = dfs(remaining_word[1:], row - 1, col) or \
            dfs(remaining_word[1:], row + 1, col) or \
            dfs(remaining_word[1:], row, col - 1) or \
            dfs(remaining_word[1:], row, col + 1)
            
            board[row][col] = temp
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                ans = ans or dfs(word, r, c)

        return ans

                


