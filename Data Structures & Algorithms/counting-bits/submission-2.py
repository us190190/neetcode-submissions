class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        for i in range(n+1):
            count_bits = 0
            current = i
            while current:
                count_bits += current%2
                current >>= 1
            res.append(count_bits)
        
        return res



        