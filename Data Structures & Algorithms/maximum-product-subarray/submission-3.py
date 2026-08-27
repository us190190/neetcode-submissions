class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_min, cur_max, res = 1, 1, nums[0]

        for num in nums:
            tmp = cur_max * num
            cur_max = max(num, tmp, cur_min * num)
            cur_min = min(num, tmp, cur_min * num)
            res = max(res, cur_max)
        
        return res
