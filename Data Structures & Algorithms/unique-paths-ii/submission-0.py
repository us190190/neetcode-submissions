class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        paths = 0
        memo = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(r,c):
            if r==ROWS or c==COLS or obstacleGrid[r][c]==1:
                return 0
            if r==ROWS-1 and c==COLS-1:
                return 1
            
            if (r,c) not in memo:
                p = dfs(r+1,c)
                p += dfs(r,c+1)
                memo[(r,c)] = p
            return memo[(r,c)]
        
        return dfs(0,0)

        