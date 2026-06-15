class Solution:
    def climbStairs(self, n: int) -> int:

        dp = []

        for i in range(n):
            if i<2:
                dp.append(i+1)
            else:
                dp.append(dp[i-1]+dp[i-2])
        
        return dp.pop()
        