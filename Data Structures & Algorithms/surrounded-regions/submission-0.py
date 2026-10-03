class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def dfs(row: int, col: int) -> None:
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            if board[row][col] == "X" or board[row][col] == "#":
                return
            board[row][col] = "#"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for row in range(m):
            for col in range(n):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
                    