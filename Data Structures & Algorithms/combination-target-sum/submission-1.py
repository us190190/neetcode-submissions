class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def dfs(i, subset, s):
            if i==len(nums) or s>=target:
                if s==target:
                    result.append(subset.copy())
                return
            
            subset.append(nums[i])
            s += nums[i]
            dfs(i, subset, s)
            subset.pop()
            s -= nums[i]
            dfs(i+1, subset, s)
        
        dfs(0, [], 0)

        return result
        