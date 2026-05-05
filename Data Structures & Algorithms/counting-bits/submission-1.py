class Solution:
    def countBits(self, n: int) -> List[int]:

        if not n:
            return [0]
        res = [0]*(n+1)
        cur_pow = 1
        next_pow = 1*2

        for i in range(1, n+1):
            if i==next_pow:
                cur_pow = next_pow
                next_pow *= 2
            res[i] = 1 + res[i-cur_pow]
        
        return res



        