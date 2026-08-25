class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # [1,2,3]
        # [2,1,3] [3,2,1]
        # [2,3,1] [3,1,2]

        self.result = []

        def dfs(i: int, perm: List[int]):
            if i == len(nums)-1:
                self.result.append(perm.copy())
                return
            
            dfs(i+1, perm)
            for idx in range(i+1, len(nums)):
                perm[i], perm[idx] = perm[idx], perm[i]
                dfs(i+1, perm)
                perm[i], perm[idx] = perm[idx], perm[i]
        
        dfs(0, nums)

        return self.result
            

        