class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        window = []

        for num in nums:
            window.append(num)
            if len(window)==k:
                m = float("-inf")
                for n in window:
                    m = max(m, n)
                result.append(m)
                window.pop(0)
        
        return result



        