
class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        
        edges = []

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                u, v = points[i], points[j]
                distance = abs(u[0]-v[0]) + abs(u[1]-v[1]) 
                edge = (i, j, distance)
                edges.append(edge)
        
        adj = [set() for _ in range(len(points))]

        for u,v,distance in edges:
            adj[u].add((distance, v))
            adj[v].add((distance, u))

        min_heap = []
        heapq.heappush(min_heap, (0,0))

        visited = set()

        total_cost = 0

        while min_heap:
            distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            total_cost += distance
            visited.add(u)
            for d, v in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (d, v))
        
        return total_cost
            


        
        



        
        