from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Maintain a set of visited points and a priority queue where the head of the pq is 
        # the point that has the smallest distance to any point in the visited set
        if len(points) == 1:
            return 0
        visited = set()
        pq = []
        res = 0
        heappush(pq, (0, points[0]))
        while pq:
            cost, curr_point = heappop(pq)
            if tuple(curr_point) in visited:
                continue
            visited.add(tuple(curr_point))
            res += cost
            if len(visited) == len(points):
                return res
            for point in points:
                if tuple(point) not in visited:
                    distance = abs(point[0] - curr_point[0]) + abs(point[1] - curr_point[1])
                    heappush(pq, (distance, point))
        return res
        