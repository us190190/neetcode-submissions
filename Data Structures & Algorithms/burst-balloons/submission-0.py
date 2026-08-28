class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1]+nums+[1]
        memo = {}

        def dfs(l, r):
            if l+1==r:
                return 0
            
            if (l,r) not in memo:
                max_coins = 0
                for i in range(l+1,r):
                    step_coins = nums[l] * nums[i] * nums[r]
                    max_coins = max(max_coins, step_coins + dfs(l,i) + dfs(i,r))
                memo[(l,r)] = max_coins
            
            return memo[(l,r)]
        
        return dfs(0, len(nums)-1)