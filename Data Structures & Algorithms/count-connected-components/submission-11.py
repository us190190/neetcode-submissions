class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [set() for _ in range(n)]

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)

        self.visited = set()
        count = 0
        
        def bfs(node):

            q = deque()
            q.append((node, -1))

            while q:
                nde, parent = q.popleft()
                self.visited.add(nde)
                for nbr in adj[nde]:
                    if nbr!=parent and nbr not in self.visited:
                        q.append((nbr, nde))
        
        for nde in range(n):
            if nde not in self.visited:
                count += 1
                bfs(nde)
        
        return count


        