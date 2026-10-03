class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(row: int, col: int, hashSet, prevHeight: int) -> None:
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            if (row, col) in hashSet:
                return
            if heights[row][col] >= prevHeight:
                hashSet.add((row, col))
                prevHeight = heights[row][col]
                dfs(row - 1, col, hashSet, prevHeight)
                dfs(row + 1, col, hashSet, prevHeight)
                dfs(row, col - 1, hashSet, prevHeight)
                dfs(row, col + 1, hashSet, prevHeight)
                
        for i in range(n):
            dfs(0, i, pacific, heights[0][i])
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
        for i in range(n):
            dfs(m - 1, i, atlantic, heights[m - 1][i])
        for i in range(m):
            dfs(i, n - 1, atlantic, heights[i][n - 1])
    
        res = []
        for row in range(m):
            for col in range(n):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append((row, col))
        return res
        