class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1 + nums2

        A.sort()
        length = len(A)
        mid = length//2

        if length%2==0:
            return (A[mid]+A[mid-1])/2
        else:
            return A[mid]
        