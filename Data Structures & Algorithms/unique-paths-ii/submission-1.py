class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        DIRECTIONS = [[0,1], [1,0]]

        def dfs(r, c):
            if r==ROWS or c==COLS or obstacleGrid[r][c]==1:
                return 0
            if r==ROWS-1 and c==COLS-1:
                return 1
            
            if (r,c) not in dp:
                paths = 0
                for dr, dc in DIRECTIONS:
                    paths += dfs(r+dr, c+dc)
                dp[(r,c)] = paths
            return dp[(r,c)]
        
        return dfs(0,0)
        