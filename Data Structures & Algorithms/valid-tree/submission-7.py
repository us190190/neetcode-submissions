class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)>(n-1):
            return False

        adj = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        q = deque()
        q.append((0,-1))
        
        visited = set()

        while q:
            node, parent = q.popleft()
            visited.add(node)
            for nbr in adj[node]:
                if nbr != parent and nbr not in visited:
                    q.append((nbr, node))
        
        return len(visited) == n


        