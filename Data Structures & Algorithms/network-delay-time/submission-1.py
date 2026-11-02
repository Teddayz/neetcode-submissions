from heapq import heappush, heappop, heapify
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))
        queue = []
        heapify(queue)
        heappush(queue, (0, k))
        res = 0
        visited = set()

        while queue:
            cost, curr = heappop(queue)
            if curr in visited:
                continue
            visited.add(curr)
            res = max(res, cost)
            neighbours = adjList.get(curr, [])
            for neighbour, w in neighbours:
                heappush(queue, (cost + w, neighbour))

        return res if len(visited) == n else -1
            
            
