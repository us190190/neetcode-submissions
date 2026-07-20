class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid)

        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0,0))

        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            if r==ROWS-1 and c==COLS-1:
                return val
            for dr,dc in DIRECTIONS:
                dr += r
                dc += c
                if dr<0 or dr==ROWS or dc<0 or dc==COLS or (dr,dc) in visited:
                    continue
                visited.add((dr, dc))
                heapq.heappush(min_heap, (max(val, grid[dr][dc]), dr, dc))
        
        