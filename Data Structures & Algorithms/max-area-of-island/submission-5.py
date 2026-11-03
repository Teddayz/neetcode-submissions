class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        def dfs(row: int, col: int) -> int:
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(area, res)
        return res