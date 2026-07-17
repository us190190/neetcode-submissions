class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        ROTTEN, FRESH, EMPTY = 2, 1, 0
        days = 0
        q = deque()
        count_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==ROTTEN:
                    q.append((r,c))
                if grid[r][c]==FRESH:
                    count_fresh += 1
        
        while count_fresh and q:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()
                for dr,dc in DIRECTIONS:
                    dr, dc = (dr+r),(dc+c)
                    if dr>=0 and dr<ROWS and dc>=0 and dc<COLS and grid[dr][dc]==FRESH:
                        q.append((dr,dc))
                        count_fresh -= 1
                        grid[dr][dc] = ROTTEN
            days += 1
        
        return -1 if count_fresh else days
                    

            

        