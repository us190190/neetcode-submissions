class Solution:
    def rob(self, nums: List[int]) -> int:

        # 1,1,3,4

        memo = {}
        n = len(nums)

        def amount(house, start):
            if house>=n:
                return 0
            
            if (house, start) not in memo:
                memo[(house,start)] = max(nums[house] + amount(house+2, start), amount(house+1, start))
            
            return memo[(house,start)]
        
        return max(amount(0,0), amount(1,1))
        