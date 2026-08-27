class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)

        if n<2:
            return nums[0]

        def amount(house, fhr):
            if (fhr and house==(n-1)) or house>=n:
                return 0
            
            if (house, fhr) not in memo:
                memo[(house, fhr)] = max(nums[house] + amount(house+2, fhr), amount(house+1, fhr))
            
            return memo[(house, fhr)]
        
        return max(amount(0, True), amount(1, False))
            
        