class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        q = deque()
        result = []

        for dst,src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            c = q.popleft()
            result.append(c)
            for nbr in adj[c]:
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        return result if len(result)==numCourses else []


        