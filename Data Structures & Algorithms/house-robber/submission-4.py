class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)

        def dfs(i):
            if i>=n:
                return 0
            
            if i not in memo:
                memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            
            return memo[i]
        
        return max(dfs(0), dfs(1))

        