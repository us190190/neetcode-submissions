class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        if target%2 !=0:
            return False
        
        target >>= 1
        memo = {}

        def dfs(i, remaining):
            if remaining==0:
                return True
            if remaining<0:
                return False
            if i==len(nums):
                return False
            
            if (i, remaining) not in memo:
                memo[(i,remaining)] = dfs(i+1, remaining-nums[i]) or dfs(i+1, remaining)
            
            return memo[(i,remaining)]
        
        return dfs(0, target)



        