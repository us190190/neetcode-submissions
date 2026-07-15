class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.result = []

        def dfs(i, subset_version):
            if i==len(nums):
                self.result.append(subset_version.copy())
                return
            
            subset_version.append(nums[i])
            dfs(i+1, subset_version)
            subset_version.pop()
            dfs(i+1, subset_version)

        dfs(0, [])
        return self.result
            




        