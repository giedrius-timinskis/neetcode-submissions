class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for pair in prerequisites:
            course, prereq = pair[0], pair[1]
            graph[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                # Cycle detected
                return False
            
            if graph[course] == []:
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            graph[course] = []

            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True