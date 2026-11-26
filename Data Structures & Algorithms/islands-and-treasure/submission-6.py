class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = 2 ** 31 - 1
        m, n = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        frontier = deque()

        # We can start do bfs from the treasure chest and update each land with the value
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    frontier.append((0, r, c))

        while frontier:
            level, row, col = frontier.popleft()
            for dx, dy in DIRS:
                new_row = dx + row
                new_col = dy + col
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == LAND:
                    grid[new_row][new_col] = level + 1
                    frontier.append((level + 1, new_row, new_col))
