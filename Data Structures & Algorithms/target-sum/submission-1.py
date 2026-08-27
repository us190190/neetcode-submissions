class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i, target):
            if i==len(nums):
                return 1 if target==0 else 0
            
            if (i, target) not in memo:
                ways = 0
                ways += dfs(i+1, target-nums[i])
                ways += dfs(i+1, target+nums[i])
                memo[(i,target)] = ways
            
            return memo[(i,target)]
        
        return dfs(0, target)


        