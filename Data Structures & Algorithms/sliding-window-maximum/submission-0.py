class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        
        l, r, result = 0, 0, []

        while r<len(nums):
            q.append(nums[r])
            if len(q)==k:
                w_max = -10001
                for num in q:
                    w_max = max(w_max, num)
                result.append(w_max)
                q.popleft()
            r += 1
        
        return result

        