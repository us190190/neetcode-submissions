class Solution:
    def hammingWeight(self, n: int) -> int:

        # 0 1  = 1
        # 1 0  = 1
        # 1 1  = 1
        
        count = 0
        while n:

            count += 1 if n&1 == 1 else 0
            n //= 2
        
        return count



        