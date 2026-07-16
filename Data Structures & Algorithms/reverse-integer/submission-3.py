class Solution:
    def reverse(self, x: int) -> int:

        MIN = -1<<31
        MAX = (1<<31) - 1

        res = 0
        sign = -1 if x<0 else 1
        x *= sign

        while x:
            digit = int(x%10)
            x = int(x/10)
            if (res<MIN//10) or (res==MIN//10 and digit<MIN%10):
                return 0
            if (res>MAX//10) or (res==MAX and digit>MAX%10):
                return 0
            res = (res*10) + (digit*sign)
        
        return res

        
        