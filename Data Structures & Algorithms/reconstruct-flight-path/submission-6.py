class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        adjList = defaultdict(list)

        for u, v in sorted(tickets):
            adjList[u].append(v)

        def dfs(node: str) -> None:
            if not node:
                return
            while adjList[node]:
                next_node = adjList[node].pop(0)
                dfs(next_node)
            result.append(node)
        dfs('JFK')
        return result[::-1]