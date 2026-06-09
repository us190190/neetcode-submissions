class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        result, visited = False, set()
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(r, c, i):
            nonlocal result
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visited or i==len(word) or word[i]!=board[r][c]:
                if i==len(word):
                    result |= True
                return
            
            visited.add((r,c))
            for dr, dc in DIRECTIONS:
                dfs(dr+r, dc+c, i+1)
            visited.remove((r,c))

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    dfs(row, col, 0)
        
        return result
        