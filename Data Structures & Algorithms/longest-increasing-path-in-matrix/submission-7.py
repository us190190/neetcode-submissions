class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        memo = {}

        def dfs(r, c):
            
            if (r,c) not in memo:
                max_path = 1
                for dr,dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if 0<=dr<ROWS and 0<=dc<COLS and matrix[dr][dc]>matrix[r][c]:
                        max_path = max(max_path, 1 + dfs(dr,dc))

                memo[(r,c)] = max_path
            
            return memo[(r,c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
        
        return max(list(memo.values()))
        


        