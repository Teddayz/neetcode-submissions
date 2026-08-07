class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set_col = [set() for _ in range(9)]
        hash_set_row = [set() for _ in range(9)]
        matrix = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in hash_set_col[j] or val in hash_set_row[i] or val in matrix[i//3][j//3]:
                    return False
                hash_set_col[j].add(val)
                hash_set_row[i].add(val)
                matrix[i//3][j//3].add(val)
        return True

        
