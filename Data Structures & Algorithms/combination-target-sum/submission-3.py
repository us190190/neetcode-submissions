class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.result = []

        def dfs(i: int, subset: List[int], c_sum: int):
            if c_sum>target:
                return
            if c_sum == target:
                self.result.append(subset.copy())
                return
            if i == len(nums):
                return
            
            dfs(i, subset+[nums[i]], c_sum+nums[i])
            dfs(i+1, subset, c_sum)
        
        dfs(0, [], 0)

        return self.result
            
        