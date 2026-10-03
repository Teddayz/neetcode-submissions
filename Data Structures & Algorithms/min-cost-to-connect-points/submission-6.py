class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        starting_point = points[0]
        pq = []
        pq.append((0, starting_point))
        heapq.heapify(pq)
        minCost = 0
        visited = set()
        while pq:
            cost, curr_point = heapq.heappop(pq)
            # print(cost, curr_point)
            if tuple(curr_point) in visited:
                continue
            visited.add(tuple(curr_point))
            points.remove(curr_point)
            minCost += cost
            for point in points:
                manhatten_distance = abs(point[0] - curr_point[0]) + abs(point[1] - curr_point[1])
                heapq.heappush(pq, (manhatten_distance, point))

        return minCost
