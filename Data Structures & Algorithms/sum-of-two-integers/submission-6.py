class Solution:
    def getSum(self, a: int, b: int) -> int:

        result = 0
        carry = 0

        # 111
        # 101
        # 100
        # 100

        for i in range(32):
            a_bit = a&1
            b_bit = b&1
            a = a>>1
            b = b>>1

            s = a_bit+b_bit+carry

            if s==3 or s==1:
                result |= 1<<i
                carry = 1 if s==3 else 0
            elif s==2 or s==0:
                carry = 1 if s==2 else 0
        
        mask, max_int = 0xFFFFFFFF, 0x7FFFFFFF
        if result > max_int:
            result = ~(result ^ mask)

        return result





        