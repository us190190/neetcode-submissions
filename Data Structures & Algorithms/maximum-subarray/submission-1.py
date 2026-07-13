class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums)<1:
            return 0
        result, s = nums[0], 0
        for num in nums:
            if s<0:
                s = 0
            s += num
            result = max(result, s)
        return result



        