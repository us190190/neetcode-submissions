class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        l, r, res = 0, 0, 0

        c_prod = 1
        while r<len(nums):
            c_prod *= nums[r]
            while l<=r and c_prod>=k:
                c_prod //= nums[l]
                l += 1
            res += (r-l+1)
            r += 1
        
        return res



        