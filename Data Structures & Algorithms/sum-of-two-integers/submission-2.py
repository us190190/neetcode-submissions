class Solution:
    def getSum(self, a: int, b: int) -> int:

        res, carry = 0, 0
        mask, max_int = 0xFFFFFFFF, 0x7FFFFFFF

        for i in range(32):
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1

            set_bit = bit1 ^ bit2 ^ carry
            carry = (bit1 + bit2 + carry) >= 2

            res |= (set_bit << i)
        
        if res > max_int:
            res = ~(res ^ mask)
        
        return res


                    

        