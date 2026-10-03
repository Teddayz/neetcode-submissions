class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        frontier = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    frontier.append((row, col, 0))

        while frontier:
            coordinates = frontier.popleft()
            r = coordinates[0]
            c = coordinates[1]
            level = coordinates[2]
            for (newRow, newCol) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dr = newRow + r
                dc = newCol + c
                if dr < 0 or dc < 0 or dr >= m or dc >= n:
                    continue
                # if its not visited, land value is INF
                if grid[dr][dc] == 2147483647:
                    grid[dr][dc] = level + 1
                    frontier.append((dr, dc, level + 1))
            

            


        

