class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = []
        heapq.heapify(pq)

        visited = set()
        heapq.heappush(pq, (grid[0][0], 0, 0))
        minHeight = grid[0][0]
        target = grid[len(grid) - 1][len(grid) - 1]

        while pq:
            currNode = heapq.heappop(pq)
            currHeight = currNode[0]
            if currHeight == target:
                minHeight = max(minHeight, currHeight)
                break
            row = currNode[1]
            col = currNode[2]
            if currHeight in visited:
                continue
            visited.add(currHeight)
            if currHeight > minHeight:
                minHeight = currHeight
            # Add the neighbours
            if row - 1 >= 0:
                heapq.heappush(pq, (grid[row - 1][col], row - 1, col))
            if row + 1 < len(grid):
                heapq.heappush(pq, (grid[row + 1][col], row + 1, col))
            if col - 1 >= 0:
                heapq.heappush(pq, (grid[row][col - 1], row, col - 1))
            if col + 1 < len(grid[0]):
                heapq.heappush(pq, (grid[row][col + 1], row, col + 1))
        return minHeight
            