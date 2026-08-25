class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # [9,2,2,4,6,1,5]

        # [1,2,2,4,5,6,9]

        candidates.sort()
        self.result = []

        def dfs(i: int, subset: List[int], c_sum: int):
            if c_sum > target:
                return
            if c_sum == target:
                self.result.append(subset.copy())
                return
            if i == len(candidates):
                return
            
            dfs(i+1, subset+[candidates[i]], c_sum+candidates[i])
            while (i+1)<len(candidates) and candidates[i+1]==candidates[i]:
                i += 1
            dfs(i+1, subset, c_sum)
        
        dfs(0,[],0)

        return self.result