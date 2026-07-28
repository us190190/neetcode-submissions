class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        for num in nums1:
            idx = -1
            result.append(idx)
            for i in range(len(nums2)):
                if nums2[i]==num:
                    idx = i
                if idx!=-1 and i>idx and nums2[i]>num:
                    result[-1] = nums2[i]
                    break
        
        return result



        