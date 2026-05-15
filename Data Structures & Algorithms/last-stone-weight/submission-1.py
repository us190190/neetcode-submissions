class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -1*stone)
        
        while len(max_heap)>1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            if x>y:
                heapq.heappush(max_heap, -1*(x-y))
        
        return -1*max_heap[0] if len(max_heap) else 0
        