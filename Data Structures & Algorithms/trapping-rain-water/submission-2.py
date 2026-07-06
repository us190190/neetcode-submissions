class Solution:
    def trap(self, height: List[int]) -> int:

        length = len(height)
        l_h, r_h = [0]*length, [0]*length
        result = 0

        prev = 0
        for i in range(length):
            l_h[i] = max(height[i], prev)
            prev = l_h[i]
        
        nxt = 0
        for i in range(length-1, -1, -1):
            r_h[i] = max(height[i], nxt)
            nxt = r_h[i]
        
        for i in range(1, length-1):
            h = min(l_h[i-1], r_h[i+1]) - height[i]
            result += h if h>0 else 0
        
        return result

        