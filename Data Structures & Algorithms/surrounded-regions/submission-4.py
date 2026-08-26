class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        not_possible = deque()
        pending = set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    if r==0 or r==ROWS-1 or c==0 or c==COLS-1:
                        not_possible.append((r,c))
                    else:
                        pending.add((r,c))

        
        while not_possible:
            r,c = not_possible.popleft()
            for dr,dc in DIRECTIONS:
                dr += r
                dc += c
                if 0<=dr<ROWS and 0<=dc<COLS and (dr,dc) in pending:
                    pending.remove((dr,dc))
                    not_possible.append((dr,dc))
        
        for r,c in pending:
            board[r][c] = 'X'

        