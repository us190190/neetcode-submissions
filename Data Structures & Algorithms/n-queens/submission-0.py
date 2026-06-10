class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result, queens = [], []
        cols, posd, negd = set(), set(), set()

        def dfs(r):
            if len(queens)==n:
                result.append(queens.copy())
                return
            if r==n:
                return

            for c in range(n):
                if c not in cols and (r+c) not in posd and (r-c) not in negd:
                    queens.append((r,c))
                    cols.add(c)
                    posd.add(r+c)
                    negd.add(r-c)
                    dfs(r+1)
                    queens.pop()
                    cols.remove(c)
                    posd.remove(r+c)
                    negd.remove(r-c)

        dfs(0)
        boards = []
        for locations in result:
            board = ['.'*n for _ in range(n)]
            for r,c in locations:
                chrs = board[r]
                chrs = chrs[:c] + 'Q' + chrs[c+1:]
                board[r] = chrs
            boards.append(board)
        
        return boards
