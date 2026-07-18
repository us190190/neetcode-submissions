class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0

        def bfs(node):
            q = deque()
            q.append((node, -1))

            while q:
                nde, parent = q.popleft()
                visited.add(nde)
                for nbr in adj[nde]:
                    if nbr==parent or nbr in visited:
                        continue
                    q.append((nbr, nde))
        
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
        
        return count

                    
        