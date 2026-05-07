class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ref = set(nums)

        max_len = 0

        for num in nums:
            if num-1 not in ref:
                c_max = 0
                val = num
                while val in ref:
                    val += 1
                    c_max += 1
                max_len = max(max_len, c_max)
        
        return max_len
            

