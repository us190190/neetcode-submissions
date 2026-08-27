class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        n = len(coins)

        def dfs(i, target):
            if target==0:
                return 1

            if i==n or target<0:
                return 0
            
            if (i, target) not in memo:
                ways = 0
                ways += dfs(i, target-coins[i])
                ways += dfs(i+1, target)

                memo[(i, target)] = ways
            
            return memo[(i, target)]
        
        return dfs(0, amount)
            
            


        