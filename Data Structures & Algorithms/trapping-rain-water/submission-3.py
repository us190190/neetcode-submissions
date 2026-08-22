class Solution:
    def trap(self, height: List[int]) -> int:

        left_heights, right_heights = [0]*len(height), [0]*len(height)

        for i in range(1, len(height)):
            left_heights[i] = max(left_heights[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            right_heights[i] = max(right_heights[i+1], height[i+1])
        
        total_water = 0

        for i in range(len(height)):
            total_water += max(0, min(left_heights[i], right_heights[i]) - height[i])
        
        return total_water
        