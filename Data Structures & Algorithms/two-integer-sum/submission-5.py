class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ref = {}

        for idx, num in enumerate(nums):
            if target-num in ref:
                return [ref[target-num], idx]
            ref[num] = idx
        
        