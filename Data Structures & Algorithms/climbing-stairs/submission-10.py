class Solution:
    def climbStairs(self, n: int) -> int:

        # 1,2,3,4,5,6,7,8,9
       

        # w(n) = w(n-1) + w(n-2)

        memo = {}

        def ways(level):
            if level <= 2:
                return level

            if level not in memo:
                memo[level] = ways(level-1) + ways(level-2)
            
            return memo[level]
        
        return ways(n)
        