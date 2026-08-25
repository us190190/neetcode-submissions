class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.distance = math.sqrt((x*x) + (y*y))

    def __gt__(self, other: Point):
        return self.distance < other.distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []

        for x,y in points:
            heapq.heappush(h, Point(x,y))
            if len(h)>k:
                heapq.heappop(h)
        
        result = []

        while h:
            point = heapq.heappop(h)
            result.append([point.x, point.y])
        
        return result



        