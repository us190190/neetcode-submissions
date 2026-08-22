class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        print(nums)

        # i____j____k

        # [-4,(-1),-1,0,0,(0),1,1,2,4]

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k = (i+1), (len(nums)-1)
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s==0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                elif s<0:
                    j += 1
                else:
                    k -= 1
        
        return result
        
        