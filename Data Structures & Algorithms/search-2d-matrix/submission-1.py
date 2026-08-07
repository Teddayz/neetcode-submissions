class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        target_index = -1
        while left <= right:
            middle = (left + right) // 2
            if target == matrix[middle][0]:
                return True
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                left = middle + 1

        row = right

        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == matrix[row][middle]:
                return True
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                left = middle + 1

        return False
