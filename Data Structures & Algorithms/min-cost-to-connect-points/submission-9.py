from heapq import heappush, heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        min_heap = []
        heappush(min_heap, (0, points[0]))

        while min_heap:
            cost, curr_point = heappop(min_heap)
            if tuple(curr_point) in visited:
                continue
            visited.add(tuple(curr_point))
            res += cost
            for point in points:
                if tuple(point) not in visited:
                    dist = abs(point[0] - curr_point[0]) + abs(point[1] - curr_point[1])
                    heappush(min_heap, (dist, point))
        
        return res
