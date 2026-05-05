class Solution:
    def getSum(self, a: int, b: int) -> int:

        res, carry = 0, 0
        mask = 0xFFFFFFFF

        for i in range(32):
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1

            set_bit = bit1 ^ bit2 ^ carry
            carry = (bit1 + bit2 + carry) >= 2

            res |= (set_bit << i)
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res


                    

        