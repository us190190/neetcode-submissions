class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        REF = {str(num-ord('A')+1): True for num in range(ord('A'), ord('Z')+1)}
        memo = {}

        def dfs(i):
            if i>n:
                return 0
            if i==n:
                return 1
            
            if i not in memo:
                count = 0
                count += dfs(i+1) if s[i:i+1] in REF else 0
                count += dfs(i+2) if s[i:i+2] in REF else 0
                memo[i] = count
            return memo[i]
        
        dfs(0)
        return memo[0]


            





        