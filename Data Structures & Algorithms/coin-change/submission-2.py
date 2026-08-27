class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)
        n = len(coins)
        memo = {}

        def no_of_coins(target):
            if target==0:
                return 0

            if target not in memo:
                min_coins = float('inf')
                for coin in coins:
                    if target>=coin:
                        min_coins = min(min_coins, 1 + no_of_coins(target-coin))
                memo[target] = min_coins
            
            return memo[target]
        
        result = no_of_coins(amount)
        
        return result if result!=float('inf') else -1

            
                    