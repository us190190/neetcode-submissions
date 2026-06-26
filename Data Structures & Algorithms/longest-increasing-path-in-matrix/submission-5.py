class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        lip = [0]

        def dfs(r, c, prev):
            if r<0 or r>=ROWS or c<0 or c>=COLS or matrix[r][c]<=prev:
                return 0
            
            if (r,c) not in dp:
                res = 0
                for dr, dc in DIRECTIONS:
                    res = max(res, 1+dfs(dr+r, dc+c, matrix[r][c]))
                dp[(r,c)] = res
                lip[0] = max(lip[0], res)
            return dp[(r,c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, float('-inf'))
        
        return lip[0]


        