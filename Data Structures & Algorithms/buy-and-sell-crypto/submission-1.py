class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)<2:
            return 0
        
        b, s, max_profit = 0, 0, 0

        while (s+1)<len(prices):
            s += 1
            if prices[s]>prices[b]:
                max_profit = max(max_profit, prices[s]-prices[b])
            else:
                b = s
        
        return max_profit




        