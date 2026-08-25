class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        h = []

        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h)>1:
            x = -1 * heapq.heappop(h)
            y = -1 * heapq.heappop(h)

            if x==y:
                continue
            elif x>y:
                heapq.heappush(h, -(x-y))
        
        return h[0]*-1 if len(h) else 0
        