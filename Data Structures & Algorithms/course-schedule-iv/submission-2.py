class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        is_pre = [set() for _ in range(numCourses)]

        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c]==0:
                q.append(c)
        
        while q:
            node = q.popleft()
            for nbr in adj[node]:
                is_pre[nbr].add(node)
                is_pre[nbr].update(is_pre[node])
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        return [True if v in is_pre[u] else False for u,v in queries]
