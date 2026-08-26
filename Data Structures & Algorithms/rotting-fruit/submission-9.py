class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        EMPTY, FRESH, ROTTEN = 0, 1, 2

        days = 0

        rotten = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    rotten.append((r,c))
                if grid[r][c] == FRESH:
                    fresh += 1
        
        while rotten:
            length = len(rotten)
            fresh_fruit_found = False
            for _ in range(length):
                r, c = rotten.popleft()
                for dr, dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if 0<=dr<ROWS and 0<=dc<COLS and grid[dr][dc] == FRESH:
                        fresh_fruit_found = True
                        grid[dr][dc] = ROTTEN
                        fresh -= 1
                        rotten.append((dr,dc))
            days += 1 if fresh_fruit_found else 0
        
        return days if not fresh else -1
            



        