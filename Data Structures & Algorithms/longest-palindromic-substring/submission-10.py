class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = defaultdict(bool)
        count = 0
        result = ""

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                sub_s = s[i:j+1]
                length = j+1-i
                if s[i] == s[j] and (length<=3 or dp[(i+1,j-1)]):
                    dp[(i,j)] = True
                    if length>count:
                        count = length
                        result = sub_s
        
        return result

