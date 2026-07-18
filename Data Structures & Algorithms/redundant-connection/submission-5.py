class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        adj = [[] for _ in range(n+1)]
        indegree = [0]*(n+1)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in range(1, n+1):
            if indegree[i]==1:
                q.append(i)
        
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr]==1:
                    q.append(nbr)
        
        for i in range(n-1, -1, -1):
            u,v = edges[i]
            if indegree[u]==2 and indegree[v]:
                return [u,v]
        
        return []


        



        