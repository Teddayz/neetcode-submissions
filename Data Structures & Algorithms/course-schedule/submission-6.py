class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        inDegree = [0] * numCourses

        for prerequisite in prerequisites:
            course = prerequisite[0]
            prereq = prerequisite[1]
            adjList[prereq] = adjList.get(prereq, [])
            adjList[prereq].append(course)
            inDegree[course] += 1
        
        processedCourses = 0
        curr = 0
        queue = deque()
        
        while curr < numCourses:
            if inDegree[curr] == 0:
                queue.append(curr)
            curr += 1

        while queue:
            curr = queue.popleft()
            processedCourses += 1
            neighbours = adjList.get(curr, [])
            for neighbour in neighbours:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

        return processedCourses == numCourses