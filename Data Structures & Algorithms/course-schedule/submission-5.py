class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        adj = [set() for _ in range(numCourses)]
        completed_courses = set()

        for a,b in prerequisites:
            indegree[a] += 1
            adj[b].add(a)
        
        q = deque()
        for course, count in enumerate(indegree):
            if count == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            completed_courses.add(course)
            for nbr in adj[course]:
                indegree[nbr] -= 1
                if not indegree[nbr] and nbr not in completed_courses:
                    q.append(nbr)
        
        return numCourses == len(completed_courses)


        