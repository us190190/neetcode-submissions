class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        q = deque()
        q.append((0,-1))
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nb in adj[node]:
                if nb==parent:
                    continue
                if nb in visited:
                    return False
                visited.add(nb)
                q.append((nb,node))
                
        return len(visited) == n

        