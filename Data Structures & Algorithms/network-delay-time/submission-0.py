import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Since time >= 1, we can use Dijkstra's Algorithm 
        heap = []
        heapq.heapify(heap)
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))
        heapq.heappush(heap, (0, k))
        minCost = 0
        visited = set()
        while heap:
            node = heapq.heappop(heap)
            cost = node[0] 
            node_id = node[1]
            if node_id in visited:
                continue
            visited.add(node_id)
            minCost = max(cost, minCost)
            neighbours = adjList.get(node_id, [])
            for neighbour in neighbours:
                currCost = cost + neighbour[1]
                heapq.heappush(heap, (currCost, neighbour[0]))
                # break
                
        return minCost if len(visited) == n else -1
        
