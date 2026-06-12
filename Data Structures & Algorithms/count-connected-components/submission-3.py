class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        visited, count = set(), 0

        def bfs(node, parent):

            q = deque()
            q.append((node,parent))
            visited.add(node)

            while q:
                c_n, c_p = q.popleft()
                for nb in adj[c_n]:
                    if nb == c_p:
                        continue
                    if nb in visited:
                        continue
                    q.append((nb, c_n))
                    visited.add(nb)
        
        for u in range(n):
            if u not in visited:
                count += 1
                bfs(u,-1)
        
        return count

            

        