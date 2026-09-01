class Solution:
    def countBits(self, n: int) -> List[int]:
        
        

        # 0 --> 000  c(0) = 0       1
        # 1 --> 001  c(1) = 1       1  
        # 2 --> 010  c(2) = c(1)+0  2
        # 3 --> 011  c(3) = c(1)+1  2
        # 4 --> 100  c(4) = c(2)+0  4
        # 5 --> 101  c(5) = c(2)+1  4
        # 6 --> 110  c(6) = c(3)+0  4
        # 7 --> 111  c(7) = c(3)+1  4

        dp = [0]*(n+1)

        for i in range(1, n+1):
            print(f"i:{i}, i>>1:{i>>1}, i&1:{i&1}")
            dp[i] = dp[i>>1] + (i&1)
        
        return dp

