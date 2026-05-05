class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prefix, right_prefix = [1]*len(nums), [1]*len(nums)

        # 1 2 3 4 6
        # 2 1
        # 3 3
        # 4 4
        # 6 6

        product = 1
        for i in range(len(nums)):
            left_prefix[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            print(product)
            right_prefix[i] = product*left_prefix[i]
            product *= nums[i]
        
        return right_prefix




        