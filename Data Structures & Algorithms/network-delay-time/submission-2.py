from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((t, v))
        frontier = []
        heappush(frontier, (0, k))
        visited = set()
        res = 0
        while frontier:
            time, src = heappop(frontier)
            if src in visited:
                continue
            visited.add(src)
            res = max(res, time)
            neighbours = adjList.get(src, [])
            for cost, neighbour in neighbours:
                heappush(frontier, (time + cost, neighbour))
        
        return res if len(visited) == n else -1