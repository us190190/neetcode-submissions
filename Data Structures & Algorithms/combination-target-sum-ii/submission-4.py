class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        self.result = []

        def dfs(i, target, subset_version):
            if target<0:
                return
            if target==0:
                self.result.append(subset_version.copy())
                return
            if i==len(candidates):
                if target==0:
                    self.result.append(subset_version.copy())
                return
            
            subset_version.append(candidates[i])
            dfs(i+1, target-candidates[i], subset_version)
            subset_version.pop()
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i += 1
            dfs(i+1, target, subset_version)
        
        dfs(0, target, [])
        return self.result
        