class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        LOCATIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c, area):
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==0:
                return 0
            
            grid[r][c] = 0
            a = 1
            for dr, dc in LOCATIONS:
                a += dfs(r+dr, c+dc, 1+area)
            return a
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    max_area = max(max_area, dfs(r, c, 0))
        
        return max_area

        