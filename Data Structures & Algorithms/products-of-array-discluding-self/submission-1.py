class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, postfix = 1, 1
        result, prefix_nums = [0]*len(nums), []

        for num in nums:
            prefix_nums.append(prefix)
            prefix *= num
        
        for i in range(len(nums)-1, -1, -1):
            result[i] = postfix * prefix_nums[i]
            postfix *= nums[i]
        
        return result
        