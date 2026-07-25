class Solution:
    def climbStairs(self, n: int) -> int:

        # 0,1,2,3,4
        dp = {}

        def dfs(i):
            if i==n:
                return 1
            if i>n:
                return 0
            
            if i not in dp:
                dp[i] = dfs(i+2) + dfs(i+1)
            return dp[i]
        dfs(0)
        return dp[0] 
        