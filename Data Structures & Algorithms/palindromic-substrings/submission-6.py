class Solution:
    def countSubstrings(self, s: str) -> int:

        dp = defaultdict(bool)
        count = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):

                length = j+1-i
                if s[i]==s[j] and (length<=3 or dp[(i+1, j-1)]):
                    dp[(i,j)] = True
                    count += 1
                    
        
        return count
        