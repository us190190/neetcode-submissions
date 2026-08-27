class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)

        def amount(house):
            if house>=n:
                return 0
            
            if house not in memo:
                memo[house] = max(nums[house] + amount(house+2), amount(house+1))
            
            return memo[house]
        
        return max(amount(0), amount(1))
        