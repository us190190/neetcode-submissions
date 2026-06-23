class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        dp = {}
        res = [0]

        def dfs(r, c, prev):
            if r<0 or r>=ROWS or c<0 or c>=COLS or matrix[r][c]<=prev:
                return 0
            
            if (r,c) not in dp:
                m = 0
                for dr,dc in DIRECTIONS:
                    m = max(m, 1 + dfs(dr+r,dc+c, matrix[r][c]))
                dp[(r,c)] = m
                res[0] = max(res[0], m)
            return dp[(r,c)]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, float('-inf'))
        return res[0]


            

        