class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        memo = {}
        ROWS, COLS = len(triangle), len(triangle)

        def dfs(r,c):
            if r==ROWS or c==COLS:
                return 0
            
            if (r,c) not in memo:
                memo[(r,c)] = triangle[r][c] + min(dfs(r+1,c), dfs(r+1,c+1))
            return memo[(r,c)]
        
        return dfs(0,0)
        