class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [set() for _ in range(n+1)]

        for u, v, t in times:
            adj[u].add((t, v))
        
        min_heap = []
        heapq.heappush(min_heap, (0, k))
        shortest_time = {}

        while min_heap:
            time_taken, node = heapq.heappop(min_heap)
            if node in shortest_time:
                continue
            shortest_time[node] = time_taken
            for additional_time, nbr in adj[node]:
                if nbr not in shortest_time:
                    heapq.heappush(min_heap, (time_taken+additional_time, nbr))
        
        return max(shortest_time.values()) if len(shortest_time) == n else -1
