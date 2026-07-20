class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n+1)]

        for u,v,t in times:
            adj[u].append((t,v))
        
        min_heap = []
        heapq.heappush(min_heap, (0,k))
        visited = {}

        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited[node] = t
            for w,v in adj[node]:
                if v not in visited:
                    heapq.heappush(min_heap, (t+w,v))
        
        return max(visited.values()) if len(visited)==n else -1
        