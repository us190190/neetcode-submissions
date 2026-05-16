class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ref = defaultdict(int)

        for num in nums:
            ref[num] += 1
        
        max_heap = []

        for num, count in ref.items():
            heapq.heappush(max_heap, [-1*count, num])
        
        result = []
        while len(max_heap) and k:
            _, num = heapq.heappop(max_heap)
            result.append(num)
            k -= 1
        
        return result

        