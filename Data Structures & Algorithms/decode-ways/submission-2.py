class Solution:
    def numDecodings(self, s: str) -> int:

        REF, n = {}, len(s)

        for i in range(ord('A'), ord('Z')+1):
            key, val = str(i-ord('A')+1), chr(i)
            REF[key] = val 

        memo = [-1]*n

        def dfs(i):
            if i>n:
                return 0
            if i==n:
                return 1

            if memo[i]==-1:
                count = 0

                tmp = s[i:i+1]
                if tmp in REF:
                    count += dfs(i+1)

                tmp = s[i:i+2]
                if tmp in REF:
                    count += dfs(i+2)

                memo[i] = count
            return memo[i]

        dfs(0)
        return memo[0]       