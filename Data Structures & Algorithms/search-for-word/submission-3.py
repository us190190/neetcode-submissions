class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(r, c, i, visited):
            if r<0 or r==ROWS or c<0 or c==COLS or i==len(word) or (r,c) in visited:
                return False
            if board[r][c]!=word[i]:
                return False
            if board[r][c]==word[i] and (i+1)==len(word):
                return True

            visited.add((r,c))
            for dr, dc in DIRECTIONS:
                if dfs(r+dr, c+dc, i+1, visited):
                    visited.remove((r,c))
                    return True
            visited.remove((r,c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    if dfs(r, c, 0, set()):
                        print(f"r:{r} c:{c}")
                        return True
        
        return False
        