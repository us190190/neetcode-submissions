class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [{} for _ in range(len(nums))]

        def dfs(i, remaining):
            if i>=len(nums):
                return int(remaining==0)
            
            if remaining not in dp[i]:
                dp[i][remaining] = dfs(i+1, remaining-nums[i]) + dfs(i+1, remaining+nums[i])
            return dp[i][remaining]
        
        return dfs(0, target)
        