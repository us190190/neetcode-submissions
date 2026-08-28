class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dfs(i,j):
            if j==len(word2):
                return len(word1)-i
            if i==len(word1):
                return len(word2)-j
            
            if (i,j) not in memo:

                if word1[i] == word2[j]:
                    memo[(i,j)] = dfs(i+1,j+1)
                else:
                    memo[(i,j)] = 1+dfs(i+1,j+1) # replace
                    memo[(i,j)] = min(memo[(i,j)], 1+dfs(i+1,j)) # remove
                    memo[(i,j)] = min(memo[(i,j)], 1+dfs(i,j+1)) # insert
            
            return memo[(i,j)]
        
        return dfs(0,0)
        