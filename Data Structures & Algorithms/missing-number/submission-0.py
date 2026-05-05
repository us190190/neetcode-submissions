class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        first, last = 0, len(nums)

        expected_sum = (last * (last+1)) >> 1

        print(expected_sum)

        s = 0
        for n in nums:
            s += n
        
        print(s)
        
        return expected_sum - s