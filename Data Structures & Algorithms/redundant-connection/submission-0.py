class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        
        adjList = defaultdict(list)

        # This function finds whether there is connection between u and v
        def find(u: int, v: int): 
            if u == v:
                return True
            visited.add(u)
            neighbours = adjList.get(u, [])
            for neighbour in neighbours:
                if neighbour not in visited:
                    if find(neighbour, v):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if not find(u, v):
                adjList[u].append(v)
                adjList[v].append(u)
            else:
                return [u, v]
