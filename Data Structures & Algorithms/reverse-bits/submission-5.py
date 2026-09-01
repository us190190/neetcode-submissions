class Solution:
    def reverseBits(self, n: int) -> int:

        count = 32
        rev = 0

        while count:
            rev <<= 1
            rev ^= n&1
            n >>= 1
            count -= 1
        
        return rev


        