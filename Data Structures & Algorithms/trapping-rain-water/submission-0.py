class Solution:
    def trap(self, height: List[int]) -> int:

        length = len(height)
        max_left, max_right = [0]* length, [0]* length

        for i in range(length):
            max_left[i] = max(height[i-1], max_left[i-1]) if i>0 else 0
        

        for i in range(length-1, 0, -1):
            max_right[i] = max(height[i+1], max_right[i+1]) if i<length-1 else 0

        ans = 0
        for i in range(length):
            t = min(max_left[i], max_right[i]) - height[i] 
            ans += t if t>0 else 0
        
        return ans

        