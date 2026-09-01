class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [set() for _ in range(n+1)]

        for u,v,t in times:
            adj[u].add((v,t))

        min_heap = []
        heapq.heappush(min_heap, (0, k))
        shortest_time = {}

        while min_heap:
            t, u = heapq.heappop(min_heap)
            if u in shortest_time:
                continue
            shortest_time[u] = t
            for v, t1 in adj[u]:
                if v not in shortest_time:
                    heapq.heappush(min_heap, (t+t1, v))
        
        return max(list(shortest_time.values())) if len(shortest_time) == n else -1




        