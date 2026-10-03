class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()
        # From each water edge, perform dfs

        def dfs(row: int, col: int, ocean) -> None:
            ocean.add((row, col))
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow = dr + row
                newCol = dc + col
                if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n:
                    if (newRow, newCol) in ocean:
                        continue
                    if heights[row][col] <= heights[newRow][newCol]:
                        dfs(newRow, newCol, ocean)
            
        for i in range(n):
            dfs(0, i, pacific)
            dfs(m - 1, i, atlantic)
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        res = list(pacific & atlantic)
        return res