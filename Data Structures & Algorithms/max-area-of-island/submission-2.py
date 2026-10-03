class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0

        def dfs(row: int, col: int) -> int:
            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            if grid[row][col] == 0:
                return 0
            grid[row][col] = 0

            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        for row in range(m):
            for col in range(n):
                maxArea = max(maxArea, dfs(row, col))
        return maxArea