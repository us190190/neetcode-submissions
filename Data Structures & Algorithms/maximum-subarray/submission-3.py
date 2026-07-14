class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = nums[0]
        c_sum = nums[0]

        for i in range(1, len(nums)):
            if c_sum<0:
                c_sum = 0
            c_sum += nums[i]
            result = max(result, c_sum)

        return result
        