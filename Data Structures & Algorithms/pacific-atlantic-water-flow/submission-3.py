class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        pacific, atlantic = set(), set()

        def dfs(r, c, reachable, prev):
            if not (0<=r<ROWS and 0<=c<COLS and heights[r][c]>=prev and (r,c) not in reachable):
                return
            reachable.add((r,c))
            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc, reachable, heights[r][c])
        
        for r in range(ROWS):
            # pacific reachability from left side
            dfs(r, 0, pacific, heights[r][0])
            # atlantic reachability from right side
            dfs(ROWS-1-r, COLS-1, atlantic, heights[ROWS-1-r][COLS-1])
        for c in range(COLS):
            # pacific reachability from top side
            dfs(0, c, pacific, heights[0][c])
            # atlantic reachability from bottom side
            dfs(ROWS-1, COLS-1-c, atlantic, heights[ROWS-1][COLS-1-c])

        # scan all cells which are reachable from both pacific and atlantic
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result
        