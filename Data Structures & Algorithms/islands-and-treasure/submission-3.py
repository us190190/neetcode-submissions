class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF, WATER, TREASURE = 2147483647, -1, 0
        visited = set()

        def dfs(r, c, steps):
            if r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]==WATER or steps>grid[r][c]:
                return
            
            if grid[r][c]!=TREASURE:
                grid[r][c] = steps
            
            for dr,dc in DIRECTIONS:
                dfs(r+dr, c+dc, steps+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==TREASURE:
                    dfs(r,c,0)
        