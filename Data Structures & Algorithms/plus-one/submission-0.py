class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = [0]*len(digits)
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            s = digits[i]+carry
            if s==10:
                digit = 0
                carry = 1
            else:
                digit = s
                carry = 0
            result[i] = digit
        
        return [1]+result if carry else result
            
        