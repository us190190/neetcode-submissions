class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        max_area = 0

        def dfs(r, c):
            if not (0<=r<ROWS and 0<=c<COLS and grid[r][c] == 1 and (r,c) not in self.visited):
                return 0
            
            self.visited.add((r,c))
            count_land = 1
            for dr,dc in DIRECTIONS:
                count_land += dfs(r+dr, c+dc)
            
            return count_land
        
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r,c))

        return max_area
        