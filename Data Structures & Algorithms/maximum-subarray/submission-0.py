class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = -1001
        for start in range(len(nums)):
            s = 0
            for end in range(start, len(nums)):
                s += nums[end]
                result = max(result, s)
        
        return result

        