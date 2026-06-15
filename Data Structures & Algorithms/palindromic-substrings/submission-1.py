class Solution:
    def countSubstrings(self, s: str) -> int:

        result, n = 0, len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                cur_len = j-i+1
                if s[i]==s[j] and (cur_len<=3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    result += 1
        
        return result
        