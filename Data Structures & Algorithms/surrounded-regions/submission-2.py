class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        extended_boundry = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O" and (r==0 or r==ROWS-1 or c==0 or c==COLS-1):
                        extended_boundry.add((r,c))
                        q.append((r,c))
        
        while q:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()
                for dr,dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if dr<0 or dr==ROWS or dc<0 or dc==COLS or (dr,dc) in extended_boundry or board[dr][dc]=="X":
                        continue
                    extended_boundry.add((dr,dc))
                    q.append((dr,dc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O" and (r,c) not in extended_boundry:
                    board[r][c] = "X"
                    
                

        