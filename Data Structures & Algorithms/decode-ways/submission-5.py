class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        n = len(s)
        MAP = {str(idx-ord('A')+1):chr(idx) for idx in range(ord('A'), ord('Z')+1)}

        def ways(idx):
            if idx>n:
                return 0
            if idx==n:
                return 1

            if idx not in memo:
                memo[idx] = 0
                if s[idx] in MAP:
                    memo[idx] += ways(idx+1)
                if (idx+1)<n and s[idx:idx+2] in MAP:
                    memo[idx] += ways(idx+2)
            
            return memo[idx]
        
        return ways(0)





        