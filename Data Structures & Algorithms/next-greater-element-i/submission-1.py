class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # nums1 = [4,1,2]
        # nums2 = [1,3,4,2]
        
        res = [-1] * len(nums1)

        ref = {}
        for i in range(len(nums1)):
            ref[nums1[i]] = i
        
        stk = []

        for num in nums2:
            while stk and stk[-1]<num:
                top = stk.pop()
                res[ref[top]] = num
            if num in ref:
                stk.append(num)
        
        return res




        