class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [{},{}]
        n = len(nums)

        if n<2:
            return nums[0]

        def dfs(i, first_included):
            if i>=n or (first_included and i==(n-1)):
                return 0
            
            if i not in memo[first_included]:
                memo[first_included][i] = max(dfs(i+1,first_included), nums[i]+dfs(i+2,first_included))
            
            return memo[first_included][i]

        return max(dfs(0,1), dfs(1,0))
        