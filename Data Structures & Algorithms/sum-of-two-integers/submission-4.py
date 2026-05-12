class Solution:
    def getSum(self, a: int, b: int) -> int:

        result, index, carry = 0, 0, 0
        mask, max_int = 0xFFFFFFFF, 0x7FFFFFFF
        while index<32:
            a_bit = a & 1
            b_bit = b & 1
            a >>= 1
            b >>= 1

            s = a_bit ^ b_bit ^ carry

            result |= s<<index
            index += 1

            carry = (a_bit + b_bit + carry)>=2

            print(f"sum: {s}, carry: {carry}")
        
        if result > max_int:
            result = ~(result ^ mask)
        
        return result
        