class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)>(n-1):
            return False
        
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        visited = set()
        q.append((0,-1))
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nbr in adj[node]:
                if nbr==parent:
                    continue
                if nbr in visited:
                    return False
                q.append((nbr, node))
                visited.add(nbr)
        
        return len(visited)==n
        



        