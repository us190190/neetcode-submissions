class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)<2:
            return 0
        
        buy, sell, result = 0, 1, 0

        while sell<len(prices):
            diff = prices[sell] - prices[buy]
            if diff>=0:
                result = max(result, diff)
                sell += 1
            else:
                buy = sell
                sell += 1
        
        return result


        