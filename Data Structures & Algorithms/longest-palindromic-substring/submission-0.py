class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res_idx, res_len = -1, 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j] and ((j-i)<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j-i+1)>res_len:
                        res_idx, res_len = i, (j-i+1)
        
        return s[res_idx:res_idx+res_len]

        