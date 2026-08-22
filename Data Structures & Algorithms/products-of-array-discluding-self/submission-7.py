class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixes, suffixes = [1]*len(nums), [1]*len(nums)

        for idx, num in enumerate(nums):
            if idx > 0:
                prefixes[idx] = prefixes[idx-1]*nums[idx-1]
        
        for idx in range(len(nums)-1, -1, -1):
            if idx < (len(nums)-1):
                suffixes[idx] = suffixes[idx+1]*nums[idx+1]
        
        products = []
        for i in range(len(nums)):
            products.append(prefixes[i]*suffixes[i])
        
        return products





        