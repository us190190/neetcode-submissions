class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp = {}

        for index, num in enumerate(nums):
            if target-num in comp:
                return [comp[target-num], index]
            
            comp[num] = index
        
            
        