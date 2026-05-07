class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res, left, right = 0, 0, len(heights)-1
        while left<right:
            area = (right-left) * min(heights[left], heights[right])
            res = max(res, area)

            if heights[left]<heights[right]:
                left += 1
            elif heights[right]<heights[left]:
                right -= 1
            else:
                left += 1
        
        return res