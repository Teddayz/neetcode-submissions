class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        exists = False
        row = None
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][left] <= target <= matrix[mid][right]:
                row = mid
                exists = True
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        
        if not exists:
            return False
        
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False