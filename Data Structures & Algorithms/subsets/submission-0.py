class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result, subset = [], []

        def dfs(i, res):
            if i==len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)
        
        dfs(0, [])

        return result

        