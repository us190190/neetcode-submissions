class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        self.result = []

        def dfs(i, subset_version):
            if i==len(nums):
                self.result.append(subset_version.copy())
                return
            
            subset_version.append(nums[i])
            dfs(i+1, subset_version)
            subset_version.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i += 1
            dfs(i+1, subset_version)
        
        dfs(0, [])
        return self.result
        