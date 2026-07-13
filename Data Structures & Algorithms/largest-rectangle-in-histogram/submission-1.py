class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = [] # (height, start_idx)
        max_area = 0
        heights.append(0)

        for idx, h in enumerate(heights):
            start_idx = idx
            while stk and stk[-1][0]>h:
                val, start_idx = stk.pop()
                width = idx - start_idx
                max_area = max(max_area, val * width)
            stk.append([h, start_idx])
        
        
        return max_area
        