class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
            course = queue.popleft()
            neighbours = adjList.get(course, [])
            for neighbour in neighbours:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        for i in range(numCourses):
            if inDegree[i] != 0:
                return False
        return True
