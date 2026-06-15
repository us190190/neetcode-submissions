class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [-1]*len(nums)

        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i]==-1:
                memo[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return memo[i]
        
        return max(dfs(0), dfs(1))
                
        