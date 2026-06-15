class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n

        p1, p2 = 1, 2
        for i in range(2, n):
            s = p1 + p2
            p1, p2 = p2, s
        
        return p2