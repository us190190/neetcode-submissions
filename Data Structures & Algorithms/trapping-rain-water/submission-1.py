class Solution:
    def trap(self, height: List[int]) -> int:

        left, right, total_vol = [], [0]*len(height), 0

        m_height = 0
        for h in height:
            left.append(m_height)
            m_height = max(m_height, h)
        
        m_height = 0
        for i in range(len(height)-1, -1, -1):
            right[i] = m_height
            m_height = max(m_height, height[i])

        for i in range(len(height)):
            vol = min(left[i], right[i]) - height[i]
            total_vol += vol if vol>0 else 0
        
        return total_vol