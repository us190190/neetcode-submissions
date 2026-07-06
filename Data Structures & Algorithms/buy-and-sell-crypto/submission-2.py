class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length = len(prices)
        if length < 2:
            return 0
        result = 0
        min_so_far = prices[0]

        for i in range(1, length):
            profit = prices[i]-min_so_far
            result = max(result, profit)
            min_so_far = min(min_so_far, prices[i])
        
        return result





        