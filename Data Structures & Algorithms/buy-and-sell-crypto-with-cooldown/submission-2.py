class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        
        def dfs(i, buying):
            if i>=len(prices):
                return 0
            
            cooldown = dfs(i+1, buying)
            if (i, buying) not in dp:
                if buying:
                    p = dfs(i+1, not buying) - prices[i]
                else:
                    p = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(p, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)
            



        