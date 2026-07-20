class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = [[] for _ in range(n)]

        for i in range(len(edges)):
            u,v = edges[i]
            w = succProb[i]
            adj[u].append((w,v))
            adj[v].append((w,u))
        
        visited = set()
        max_heap = []
        heapq.heappush(max_heap,(-1,start_node))

        while max_heap:
            w, node = heapq.heappop(max_heap)
            if node in visited:
                continue
            visited.add(node)
            if node==end_node:
                return -w
            for p,v in adj[node]:
                if v not in visited:
                    heapq.heappush(max_heap, (w*p,v))
        
        return 0
