class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j, k = i+1, len(nums)-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s==0:
                    result.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j<k and nums[j-1]==nums[j]:
                        j += 1
                elif s<0:
                    j += 1
                else:
                    k -= 1
        
        return result




        