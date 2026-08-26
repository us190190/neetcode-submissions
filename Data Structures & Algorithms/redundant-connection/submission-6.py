class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        indegree = [0]*(n+1)
        adj = [set() for _ in indegree]

        for u,v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj[u].add(v)
            adj[v].add(u)
        
        q = deque()

        for node, count in enumerate(indegree):
            if count==1:
                q.append(node)
        
        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nbr in adj[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 1:
                    q.append(nbr)
        
        for idx in range(len(edges)-1, -1, -1):
            u,v = edges[idx]
            if indegree[u]==2 and indegree[v]==2:
                return [u,v]
        
        return []


        