class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # 0,-1,3,-4,10
        #  0, 1,3,4,10
        
        l, r = 0, len(nums)-1
        result = []

        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                result.append(nums[l]*nums[l])
                l += 1
            else:
                result.append(nums[r]*nums[r])
                r -= 1
        
        return result[::-1]



        