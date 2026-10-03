class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # I basically have to check whether there is a cycle
        if len(edges) != n - 1:
            return False
        visited = set()
        adjList = defaultdict(list)
        parent = -1

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            neighbours = adjList.get(node, [])
            for neighbour in neighbours:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
