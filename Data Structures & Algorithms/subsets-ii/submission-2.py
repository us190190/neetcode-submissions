class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        self.result = []

        def dfs(i: int, subset: List[int]):
            if i == len(nums):
                self.result.append(subset.copy())
                return
            
            dfs(i+1, subset+[nums[i]])
            while (i+1)<len(nums) and nums[i+1]==nums[i]:
                i += 1
            dfs(i+1, subset)
        
        dfs(0, [])

        return self.result
        