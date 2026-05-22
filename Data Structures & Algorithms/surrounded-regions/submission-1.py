class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[0,1], [1,0], [-1,0],[0,-1]]

        donot_cells = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (r==0 or r==ROWS-1 or c==0 or c==COLS-1) and board[r][c]=="O":
                    cell = (r,c)
                    donot_cells.add(cell)
                    q.append(cell)

        while q:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()
                for dr,dc in DIRECTIONS:
                    dr += r
                    dc += c
                    if dr<0 or dr>=ROWS or dc<0 or dc>=COLS or board[dr][dc]=="X" or (dr,dc) in donot_cells:
                        continue
                    q.append((dr,dc))
                    donot_cells.add((dr,dc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O" and (r,c) not in donot_cells:
                    board[r][c]="X"


        
        