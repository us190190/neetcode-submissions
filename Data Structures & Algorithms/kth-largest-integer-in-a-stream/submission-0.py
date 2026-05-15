class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        for num in nums:
            heapq.heappush(self.max_heap, -1*num)

    def add(self, val: int) -> int:

        heapq.heappush(self.max_heap, -1*val)

        largest = []
        for i in range(self.k):
            largest.append(heapq.heappop(self.max_heap))
        
        result = -1*largest[-1]

        for num in largest:
            heapq.heappush(self.max_heap, num)
        
        return result
