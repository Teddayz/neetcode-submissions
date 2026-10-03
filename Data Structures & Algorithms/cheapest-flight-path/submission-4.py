class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, cost in flights:
            adjList[u].append((cost, v))

        prices = [math.inf] * n
        prices[src] = 0

        iteration = 0
        while iteration < k + 1:
            prices2 = prices[:]
            for u, v, cost in flights:
                if prices[u] == math.inf:
                    continue
                if cost + prices[u] < prices2[v]:
                    prices2[v] = cost + prices[u]
            prices = prices2
                # print(prices[v])
            iteration += 1

        return prices[dst] if prices[dst] != math.inf else -1
