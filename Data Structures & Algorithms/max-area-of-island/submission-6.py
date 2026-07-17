class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0,1], [1,0], [-1,0], [0,-1]]
        visited = set()

        def dfs(r, c):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visited or grid[r][c]==0:
                return 0

            visited.add((r,c))
            a = 1
            for dr, dc in DIRECTIONS:
                a += dfs(r+dr, c+dc)
            return a

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visited:
                    max_area = max(max_area,dfs(r,c))
        
        return max_area


        