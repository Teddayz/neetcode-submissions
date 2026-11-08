from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = 2 ** 31 - 1
        m, n = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Go to each treasure and perform bfs 
        frontier = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    frontier.append((r, c, 0))

        while frontier:
            row, col, depth = frontier.popleft()
            grid[row][col] = depth
            for dr, dc in DIRS:
                new_row, new_col = dr + row, dc + col
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == LAND:
                    grid[new_row][new_col] = depth + 1
                    frontier.append((new_row, new_col, depth + 1))
        


