class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford algorithm.
        # Start is 0, everything else is max
        # After each iteration, we get the 
        adjList = defaultdict(list)
        for u, v, cost in flights:
            adjList[u].append((cost, v))
        queue = []
        queue.append((0, src, 0))
        heapq.heapify(queue)
        minCost = {}
        while queue:
            node = heapq.heappop(queue)
            cost = node[0]
            curr = node[1]
            level = node[2]
            if curr == dst:
                return cost
            if level > k:
                continue
            if curr in minCost and minCost[curr] <= level:
                continue
            minCost[curr] = level
            neighbours = adjList.get(curr, [])
            for neighbour in neighbours:
                heapq.heappush(queue, (neighbour[0] + cost, neighbour[1], level + 1))

        return -1

        