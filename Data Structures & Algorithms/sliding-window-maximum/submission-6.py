class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = []
        
        result = []

        for idx, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, idx))
            if len(max_heap)>k:
                while max_heap and max_heap[0][1] < (idx-k+1):
                    heapq.heappop(max_heap)
            if len(max_heap)>=k:
                result.append(-max_heap[0][0])
        
        return result



        
        