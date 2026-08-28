class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(cur_nums):
            if len(cur_nums)==0:
                return 0
            
            if cur_nums not in memo:
                max_coins = 0
                for i in range(len(cur_nums)):
                    left_coins = cur_nums[i-1] if (i-1)>=0 else 1
                    right_coins = cur_nums[i+1] if (i+1)<len(cur_nums) else 1
                    step_coins = left_coins * cur_nums[i] * right_coins
                    new_nums = tuple(cur_nums[:i] + cur_nums[i+1:])
                    max_coins = max(max_coins, step_coins + dfs(new_nums))
                memo[cur_nums] = max_coins
            
            return memo[cur_nums]
        
        return dfs(tuple(nums))