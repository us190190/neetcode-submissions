class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = []
        max_area = 0
        heights.append(0)

        for idx, height in enumerate(heights):
            new_idx = idx
            while stk and stk[-1][1]>=height:
                new_idx, p_height = stk.pop()
                area = (idx-new_idx)*p_height
                max_area = max(max_area, area)
            stk.append((new_idx, height))
        
        return max_area

        