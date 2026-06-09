class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def dfs(i, subset, s):
            if s==target:
                result.append(subset.copy())
                return
            if i==len(candidates) or s>target:
                return
            
            subset.append(candidates[i])
            s += candidates[i]
            dfs(i+1, subset, s)
            subset.pop()
            s -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subset, s)
        
        dfs(0, [], 0)

        return result
        