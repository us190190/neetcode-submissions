class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # [2,20,4,10,3,4,5]
        # [4, 3,3, 3,3,2,1]

        if len(nums)<1:
            return 0
        
        result = 1
        ref = {}
        for num in nums:
            ref[num] = 0

        for cur in nums:
            prv = cur-1
            if prv not in ref:
                length = 1
                while (cur+length) in ref:
                    length += 1
                result = max(result, length)
        
        return result




        