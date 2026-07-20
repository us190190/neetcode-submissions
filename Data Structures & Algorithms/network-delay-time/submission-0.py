class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = [[] for _ in range(n+1)]
        
        for src, dst, w in times:
            adj[src].append((w, dst))
        
        shortest = {}
        min_heap = []
        heapq.heappush(min_heap, (0,k))

        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in shortest:
                continue
            shortest[node] = t
            for w, dst in adj[node]:
                if dst not in shortest:
                    heapq.heappush(min_heap, (t+w, dst))
        
        return max(shortest.values()) if len(shortest)==n else -1




        