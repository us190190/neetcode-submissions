class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0,1], [1,0], [-1,0], [0,-1]]
        max_area = 0

        def dfs(r, c, area):
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==0:
                return area
            area += 1
            grid[r][c] = 0
            for dr,dc in DIRECTIONS:
                area = max(area, dfs(r+dr, c+dc, area))
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    max_area = max(max_area, dfs(r,c,0))
        
        return max_area

        