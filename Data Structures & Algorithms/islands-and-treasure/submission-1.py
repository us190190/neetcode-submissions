class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS, INF = len(grid), len(grid[0]), 2147483647
        DIRECTIONS = [[0,1], [1,0], [-1,0], [0,-1]]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        steps = 0
        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                for dr,dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if dr<0 or dr>=ROWS or dc<0 or dc>=COLS or grid[dr][dc]==-1 or grid[dr][dc]==0:
                        continue
                    if grid[dr][dc]==INF:
                        grid[dr][dc] = steps+1
                        q.append((dr,dc))
            steps += 1
        