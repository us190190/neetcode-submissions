class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        cell = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val=='.':
                    continue
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                idx = str(r//3)+"_"+str(c//3)
                if val in cell[idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                cell[idx].add(val)

        return True 


        