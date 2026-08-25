class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #. ABCESEEEFS
        
        # ["A","B","C","E"],
        # ["S","F","E","S"],
        # ["A","D","E","E"]

        self.visited = set()
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(i:int, r: int, c: int) -> bool:
            if i == len(word):
                return True
            if not (0<=r<ROWS) or not (0<=c<COLS) or (r,c) in self.visited:
                return False
            
            if word[i] == board[r][c]:
                self.visited.add((r,c))
                for dr,dc in DIRECTIONS:
                    if dfs(i+1, r+dr, c+dc):
                        return True
                self.visited.remove((r,c))
            
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if word[0] == board[r][c]:
                    self.visited = set()
                    if dfs(0, r, c):
                        return True
        
        return False
                


        