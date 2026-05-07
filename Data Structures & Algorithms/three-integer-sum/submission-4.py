class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()
        nums_len = len(nums)

        for i in range(nums_len-2):
            left = i+1
            right = nums_len-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if s<0:
                    left += 1
                elif s>0:
                    right -= 1
                else:
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
        
        return list(res)

        