class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].add(a)
        
        q = deque()
        for course, count in enumerate(indegree):
            if count == 0:
                q.append(course)
        
        completed_courses = set()
        sequence = []

        while q:
            course = q.popleft()
            completed_courses.add(course)
            sequence.append(course)
            for nbr in adj[course]:
                indegree[nbr] -= 1
                if not indegree[nbr] and nbr not in completed_courses:
                    q.append(nbr)

        return sequence if len(completed_courses) == numCourses else []
        