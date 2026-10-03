class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        inDegree = [0] * (len(edges) + 1)
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            inDegree[u] += 1
            inDegree[v] += 1

        queue = deque()
        curr = 1
        while curr <= len(edges):
            if inDegree[curr] == 1:
                queue.append(curr)
            curr += 1

        while queue:
            node = queue.popleft()
            neighbours = adjList.get(node, [])
            for neighbour in neighbours:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 1:
                    queue.append(neighbour)
        
        cycleNodes = set()

        for i in range(len(edges) + 1):
            if i == 0:
                continue
            if inDegree[i] > 1:
                cycleNodes.add(i)
        for u, v in reversed(edges):
            if u in cycleNodes and v in cycleNodes:
                return [u, v]
        return []


        

