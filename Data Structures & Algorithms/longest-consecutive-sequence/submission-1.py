class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        reference = set(nums)

        max_length = 0

        for num in nums:
            if num-1 not in reference:
                length = 0
                i = num
                while i in reference:
                    length += 1
                    i += 1
                    max_length = max(max_length, length)
        
        return max_length

