class Location:
    def __init__(self, point: List[int]):
        self.x = point[0]
        self.y = point[1]
        self.distance = (self.x*self.x) + (self.y*self.y)
    
    def __lt__(self, other) -> bool:
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_h = []

        for point in points:
            heapq.heappush(min_h, Location(point))
        
        result = []

        while len(result)<k and len(min_h):
            loc = heapq.heappop(min_h)
            result.append([loc.x, loc.y])
        
        return result


        