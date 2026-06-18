class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        MAX_INT = 110000
        memo = {}
        
        def dfs(remaining):
            if not remaining:
                return 0
            
            if remaining not in memo:
                min_count = MAX_INT
                for coin in coins:
                    if remaining>=coin:
                        min_count = min(min_count, 1+dfs(remaining-coin))
                memo[remaining] = min_count
            return memo[remaining]
        
        result = dfs(amount)
        return result if result!= MAX_INT else -1

        