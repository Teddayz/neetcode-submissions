class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        heapq.heapify(pq)

        heapq.heappush(pq, (0, points[0]))
        visited = set()
        minCost = 0
        while pq:
            cost, point = heapq.heappop(pq)
            # print(cost, point)
            if not point or cost == math.inf:
                break
            if tuple(point) in visited:
                continue
            minCost += cost
            visited.add(tuple(point))
            points.remove(point)
            min_manhatten_distance = math.inf
            nextPoint = None
            # Get the smallest edge from this point
            for coordinate in points:
                manhatten_distance = abs(coordinate[0] - point[0]) + abs(coordinate[1] - point[1])
                if manhatten_distance < min_manhatten_distance:
                    min_manhatten_distance = manhatten_distance
                    nextPoint = coordinate
                heapq.heappush(pq, (manhatten_distance, coordinate))

        return minCost 
