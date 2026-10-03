class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        top = [1] * n
        left = [1] * m

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    top[c] = 0
                    left[r] = 0
        for c in range(n):
            if top[c] == 0:
                for r in range(m):
                    matrix[r][c] = 0
        for r in range(m):
            if left[r] == 0:
                for c in range(n):
                    matrix[r][c] = 0
        

        