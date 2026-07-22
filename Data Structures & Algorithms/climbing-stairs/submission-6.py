class Solution:
    def climbStairs(self, n: int) -> int:

        # 0,1,2,3,4,5,6
        #13,8,5,3,2,1,1


        memo = {}
        def dfs(i):
            if i>n:
                return 0
            if i==n:
                return 1
            
            if i not in memo:
                memo[i] = dfs(i+1) + dfs(i+2)
            
            return memo[i]
        
        dfs(0)
        return memo[0]
            