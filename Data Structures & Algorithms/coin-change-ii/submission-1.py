class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()
        dp = [[-1]*(amount+1) for _ in range(len(coins))]

        def dfs(i, target):
            if i>=len(coins):
                return 0
            if target == 0:
                return 1
            
            if dp[i][target]==-1:
                ways = 0
                if coins[i]<=target:
                    ways += dfs(i,target-coins[i])
                    ways += dfs(i+1, target)
                dp[i][target] = ways
            return dp[i][target]
        
        return dfs(0, amount)
            

        