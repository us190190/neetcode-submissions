class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for dst,src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        result = []
        while q:
            node = q.popleft()
            if node in result:
                return []
            result.append(node)
            for nbr in adj[node]:
                if nbr in result:
                    return []
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        return result if len(result)==numCourses else []

        