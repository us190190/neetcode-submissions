class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        self.visited = set()

        def dfs(r, c):
            if not (0<=r<ROWS and 0<=c<COLS and grid[r][c]=="1" and (r,c) not in self.visited):
                return 0
            
            self.visited.add((r,c))
            for dr,dc in DIRECTIONS:
                dfs(r+dr, c+dc)
            
            return 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += dfs(r, c)
        
        return count
        