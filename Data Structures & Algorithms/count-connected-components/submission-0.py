class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        count = 0
        visited = set()

        def dfs(node: int, parent: int):
            visited.add(node)
            neighbours = adjList.get(node, [])
            for neighbour in neighbours:
                if neighbour == parent: 
                    continue
                if neighbour not in visited:
                    dfs(neighbour, node)


        for i in range(n):
            if i in visited:
                continue
            count += 1
            dfs(i, -1)
            
        return count