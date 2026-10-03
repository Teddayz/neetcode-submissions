class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        adjList = {}
        for prerequisite in prerequisites:
            course = prerequisite[0]
            if course not in adjList:
                adjList[course] = []
            adjList[course].append(prerequisite[1])
        def dfs(course: int, path) -> bool:
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            dependencies = adjList.get(course, [])
            for dependency in dependencies:
                if not dfs(dependency, path):
                    return False
            path.remove(course)
            visited.add(course)
            return True


        course = 0
        while course < numCourses:
            path = set()
            if course not in visited:
                if not dfs(course, path):
                    return False
            course += 1

        return True