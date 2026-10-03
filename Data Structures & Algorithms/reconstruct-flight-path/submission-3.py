class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        adjList = defaultdict(deque)
        # Populate the neighbours
        for u, v in sorted(tickets):
            adjList[u].append(v)

        
        def dfs(node: str):
            if not node:
                return
            while adjList[node]:
                next_node = adjList[node].popleft()
                dfs(next_node)
                    
            result.append(node)
        
        dfs('JFK')
        return result[::-1]