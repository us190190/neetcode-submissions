class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # [1,2,3]
        # [],           [1]
        # []     [2]         [1]         [1,2]
        # [][3]. [2][2,3].   [1][1,3].   [1,2] [1,2,3] 
        self.result = []

        def dfs(i: int, subset: List[int]):
            if i == len(nums):
                self.result.append(subset.copy())
                return
            
            dfs(i+1, subset)
            dfs(i+1, subset+[nums[i]])
        
        dfs(0, [])

        return self.result
        