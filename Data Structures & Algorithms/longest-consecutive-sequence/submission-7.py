class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        result = 0
        exists = set(nums)
        
        for num in nums:
            prev = num-1
            if prev not in exists:
                depth = 1
                while (num+depth) in exists:
                    depth += 1
                result = max(result, depth)

        return result






        