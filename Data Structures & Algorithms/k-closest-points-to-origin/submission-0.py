
class PointsWrapper:
    def __init__(self, point):
        self.point = point
        self.distance = math.sqrt((point[0]*point[0]) + (point[1]*point[1]))
    
    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []

        for point in points:
            heapq.heappush(min_heap, PointsWrapper(point))
        
        result = []
        while k:
            val = heapq.heappop(min_heap)
            result.append(val.point)
            k -= 1
        
        return result
        