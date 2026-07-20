class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        is_pre = [set() for _ in range(numCourses)]
        while q:
            node = q.popleft()
            for nbr in adj[node]:
                is_pre[nbr].add(node)
                is_pre[nbr].update(is_pre[node])
                indegree[nbr] -= 1
                if indegree[nbr]==0:
                    q.append(nbr)
        
        ans = []
        for u,v in queries:
            status = True if u in is_pre[v] else False
            ans.append(status)
        
        return ans



