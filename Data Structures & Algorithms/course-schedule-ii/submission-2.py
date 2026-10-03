class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        inDegree = [0] * numCourses
        adjList = {}

        for course, prereq in prerequisites:
            adjList[prereq] = adjList.get(prereq, [])
            adjList[prereq].append(course)
            inDegree[course] += 1
        
        queue = deque()
        curr = 0
        processedCourses = 0
        while curr < numCourses:
            if inDegree[curr] == 0:
                queue.append(curr)
            curr += 1
        
        while queue:
            course = queue.popleft()
            result.append(course)
            processedCourses += 1
            neighbours = adjList.get(course, [])
            for neighbour in neighbours:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        return result if processedCourses == numCourses else []
