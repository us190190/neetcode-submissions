class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)<2:
            return 0
        
        buy = prices[0]
        result = 0

        for sell in prices:

            if sell<buy:
                buy = sell
            
            profit = sell-buy
            result = max(result, profit)
        
        return result
            
        