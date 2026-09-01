class Solution:
    def getSum(self, a: int, b: int) -> int:

        # 4 100
        # 7 111
        #   ___
        #  1011

        s, c = 0, 0

        count = 0
        while count<32:
            b1 = a&1
            b2 = b&1
            a >>= 1
            b >>= 1
            tmp_s = b1 ^ b2 ^ c
            
            c = (b1&b2) | (b1&c) | (b2&c)
            s |= tmp_s<<count
            
            count += 1
        
        return s if s < 0x7FFFFFFF else ~(s ^ 0xFFFFFFFF)