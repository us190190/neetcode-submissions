class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visited or grid[r][c]=="0":
                return
            visited.add((r,c))
            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    count += 1

        return count

        