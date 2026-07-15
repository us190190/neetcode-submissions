class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.h = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:

        heapq.heappush(self.h, val)
        if len(self.h)>self.k:
            heapq.heappop(self.h)
        
        return self.h[0]
        
