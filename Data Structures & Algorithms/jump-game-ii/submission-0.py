class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i):
            if i==(len(nums)-1):
                return 0
            
            if i not in memo:
                m = 1001
                for itr in range(i+1, min(len(nums), i+nums[i]+1)):
                    m = min(m, 1+dfs(itr))
                memo[i] = m
            return memo[i]
        
        return dfs(0)
        