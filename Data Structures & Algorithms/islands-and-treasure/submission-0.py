class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        frontier = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    frontier.append((row - 1, col, 1))
                    frontier.append((row + 1, col, 1))
                    frontier.append((row, col - 1, 1))
                    frontier.append((row, col + 1, 1))

        while frontier:
            coordinates = frontier.popleft()
            r = coordinates[0]
            c = coordinates[1]
            level = coordinates[2]
            if r < 0 or c < 0 or r >= m or c >= n:
                continue
            # if its not visited, land value is INF
            if grid[r][c] == 2147483647:
                grid[r][c] = level
                frontier.append((r - 1, c, level + 1))
                frontier.append((r + 1, c, level + 1))
                frontier.append((r, c - 1, level + 1))
                frontier.append((r, c + 1, level + 1))
            

            


        

