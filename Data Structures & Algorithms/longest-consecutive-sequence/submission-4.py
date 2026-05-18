class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ref, result = set(nums), 0

        for num in nums:
            if num-1 not in ref:
                c_max = 0
                val = num
                while val in ref:
                    c_max += 1
                    val += 1
                    result = max(result, c_max)
        
        return result

        