class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        result = 0
        stk = []
        heights.append(0)

        for i in range(len(heights)):
            start = i
            while len(stk) and heights[i]<stk[-1][1]:
                start, val = stk.pop()
                width = i - start
                result = max(result, val*width)
            stk.append((start, heights[i]))
        
        return result       