class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands, ROWS, COLS = 0, len(grid), len(grid[0])
        DIRECTIONS = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(r,c):
            if r<0 or r >= ROWS or c<0 or c >= COLS or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            for row, col in DIRECTIONS:
                dfs(r+row, c+col)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
            


        