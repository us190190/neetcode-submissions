class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0,1], [1,0], [-1,0], [0,-1]]

        q, fresh = deque(), 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh += 1
        
        days = 0
        while fresh and q:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()
                for dr,dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if dr<0 or dr>=ROWS or dc<0 or dc>=COLS:
                        continue
                    if grid[dr][dc]==1:
                        fresh -= 1
                        grid[dr][dc]=2
                        q.append((dr,dc))
            days += 1
        
        return days if fresh==0 else -1


        