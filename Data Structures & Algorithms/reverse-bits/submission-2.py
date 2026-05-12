class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0
        index = 31
        while n:
            c_bit = n & 1
            n >>= 1
            result |= c_bit<<index
            index -= 1
        
        return result
        