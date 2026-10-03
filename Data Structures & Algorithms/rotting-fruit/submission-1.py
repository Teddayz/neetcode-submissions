class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        m = len(grid)
        n = len(grid[0])
        frontier = deque()
        # Adding all the rotten fruit
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    frontier.append((row, col, 0))

        while frontier:
            node = frontier.popleft()
            minutes = max(minutes, node[2])
            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                newRow = node[0] + dr
                newCol = node[1] + dc
                if newRow < 0 or newCol < 0 or newRow >= m or newCol >= n:
                    continue
                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    frontier.append((newRow, newCol, node[2] + 1))
        valid = True
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    valid = False
        return minutes if valid else -1

        