class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set_col = set()
        hash_set_square = set()
        matrix = [[set() for _ in range(3)] for _ in range(3)]

        for row in board:
            if self.hasDuplicate(row):
                return False
        
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in hash_set_col:
                    return False
                hash_set_col.add(board[i][j])
            hash_set_col.clear()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                square_row_index = i // 3
                square_col_index = j // 3
                if board[i][j] in matrix[square_row_index][square_col_index]:
                    return False
                matrix[square_row_index][square_col_index].add(board[i][j])
        return True
                
        

    def hasDuplicate(self, nums: List[str]) -> bool:
        hash_set = set()
        for num in nums:
            if num == ".":
                continue
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
