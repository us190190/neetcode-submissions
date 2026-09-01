class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [set() for _ in range(n)]

        for s, d, cost in flights:
            adj[s].add((cost, d))
        
        min_heap = []
        heapq.heappush(min_heap, (0, 0, src))
        visited_stops = [float('inf') for _ in range(n)]

        while min_heap:
            cost, stops, s = heapq.heappop(min_heap)
            if s == dst:
                return cost
            if stops>k or stops>=visited_stops[s]:
                continue
            visited_stops[s] = stops
            for add_cost, d in adj[s]:
                heapq.heappush(min_heap, (cost+add_cost, stops+1, d)) 
        
        return -1
        