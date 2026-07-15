class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_h = []

        for stone in stones:
            heapq.heappush(max_h, -stone)
        
        while len(max_h)>1:
            first = -heapq.heappop(max_h)
            second = -heapq.heappop(max_h)
            if first > second:
                heapq.heappush(max_h, -(first-second))
            else:
                heapq.heappush(max_h, 0)
        
        return -max_h[0]

        