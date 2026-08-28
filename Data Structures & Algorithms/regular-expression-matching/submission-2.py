class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dfs(i,j):
            if j == len(p):
                return i == len(s)
            
            if (i,j) not in memo:

                match = i<len(s) and (s[i]==p[j] or p[j]=='.')
                status = False

                if (j+1)<len(p) and p[j+1]=='*':
                    status = dfs(i, j+2) or (match and dfs(i+1, j))
                else:
                    status = dfs(i+1, j+1) if match else False

                memo[(i,j)] = status
            
            return memo[(i,j)]
        
        return dfs(0,0)


        