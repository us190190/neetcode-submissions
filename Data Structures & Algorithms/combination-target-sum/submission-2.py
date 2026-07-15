class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.result = []

        def dfs(i, target, subset_version):
            if target<0:
                return
            if target==0:
                self.result.append(subset_version.copy())
                return
            if i==len(nums):
                if target==0:
                    self.result.append(subset_version.copy())
                return
            
            subset_version.append(nums[i])
            dfs(i, target-nums[i], subset_version)
            subset_version.pop()
            dfs(i+1, target, subset_version)
        
        dfs(0, target, [])
        return self.result



        