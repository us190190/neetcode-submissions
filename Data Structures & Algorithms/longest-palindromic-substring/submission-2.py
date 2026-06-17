class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res_idx, res_len = 0, 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                cur_len = j-i+1
                if s[i]==s[j] and (cur_len<=3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if cur_len>res_len:
                        res_idx = i
                        res_len = cur_len
        
        return s[res_idx:res_idx+res_len]
                
        