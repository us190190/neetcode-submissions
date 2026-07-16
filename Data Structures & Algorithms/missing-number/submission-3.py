class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)

        result = length

        for i in range(length):
            result = result ^ i ^ nums[i]
        
        return result
        