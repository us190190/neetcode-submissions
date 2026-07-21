class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = [[] for _ in range(len(points))]

        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        
        min_heap = []
        visited = set()
        heapq.heappush(min_heap, (0,0))

        cost = 0
        while min_heap:
            dist, pt = heapq.heappop(min_heap)
            if pt in visited:
                continue
            visited.add(pt)
            cost += dist
            for d, nbr in adj[pt]:
                if nbr not in visited:
                    heapq.heappush(min_heap, (d,nbr))
        
        return cost
                


        