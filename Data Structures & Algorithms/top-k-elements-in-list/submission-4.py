class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ref = defaultdict(int)

        for num in nums:
            ref[num] += 1
        
        min_heap = []

        for num, count in ref.items():
            heapq.heappush(min_heap, [count, num])
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        result = []
        while len(min_heap):
            _, num = heapq.heappop(min_heap)
            result.append(num)
        
        return result

        