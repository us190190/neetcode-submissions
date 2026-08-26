class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        [4,-1,0,1],
        [3,2,1,-1],
        [1,-1,2,-1],
        [0,-1,3,4]

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        LAND, WATER, TREASURE = 2147483647, -1, 0

        level = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == TREASURE:
                    level.append((r,c))
        

        distance = 0

        while level:
            length = len(level)
            for _ in range(length):
                r, c = level.popleft()
                for dr, dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if 0<=dr<ROWS and 0<=dc<COLS and grid[dr][dc] == LAND:
                        grid[dr][dc] = distance + 1
                        level.append((dr, dc))
            distance += 1
            

        


        