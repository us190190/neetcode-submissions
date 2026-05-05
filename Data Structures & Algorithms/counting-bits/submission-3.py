class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0]*(n+1)
        cur_pow = 1
        next_pow = 2

        for i in range(1, n+1):
            if i==next_pow:
                cur_pow = next_pow
                next_pow *= 2
            res[i] = 1 + res[i-cur_pow]
        
        return res
        
    # O(n log n)
    # def countBits(self, n: int) -> List[int]:

    #     res = []

    #     for i in range(n+1):
    #         count_bits = 0
    #         current = i
    #         while current:
    #             count_bits += current%2
    #             current >>= 1
    #         res.append(count_bits)
        
    #     return res



        