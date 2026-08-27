class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        n = len(prices)

        def dfs(i):
            if i>=n:
                return 0
            
            if i not in memo:
                max_profit = float('-inf')
                for idx in range(i+1, n):
                    if prices[idx]>prices[i]:
                        max_profit = max(max_profit, prices[idx]-prices[i] + dfs(idx+2))
                
                max_profit = max(max_profit,dfs(i+1))
                
                memo[i] = max_profit
            
            return memo[i]
        
        return dfs(0)


        