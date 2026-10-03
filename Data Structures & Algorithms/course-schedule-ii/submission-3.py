class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []
        adjList = defaultdict(list)
        inDegree = [0] * numCourses
        for u, v in prerequisites:
            adjList[v].append(u)
            inDegree[u] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            neighbours = adjList.get(curr, [])
            res.append(curr)
            for neighbour in neighbours:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
            
        return res if len(res) == numCourses else []