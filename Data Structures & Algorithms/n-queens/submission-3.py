class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = ['.' * n for _ in range(n)]
        def backtrack(col: int, curr: List[List[str]]) -> None:
            if col >= n:
                res.append(curr.copy())
                return
            for r in range(n):
                if self.isValidPlacement(r, col, curr):
                    curr[r] = curr[r][0:col] + "Q" + curr[r][col + 1:]
                    backtrack(col + 1, curr)
                    curr[r] = curr[r][:col] + "." + curr[r][col + 1:]

        backtrack(0, curr)
            
        return res

    def isValidPlacement(self, row: int, col: int, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            # Check for each row whether there is a Q
            if board[i][col] == "Q":
                return False
            # Check for each col whether there is a Q
            if board[row][i] == "Q":
                return False
                    
        # Check diagonal -> left only
        # Top left
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        # Bottom left
        
        r, c = row + 1, col - 1
        while r < n and col >= 0:
            if board[r][c] == "Q":
                return False
            r += 1
            c -= 1
        
        
        return True
        