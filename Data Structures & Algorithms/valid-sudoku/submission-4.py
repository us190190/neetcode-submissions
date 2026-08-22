class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        subgrids = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                grid_idx = tuple([r//3,c//3])
                val = board[r][c]
                if val == ".":
                    continue
                if val not in rows[r] and val not in cols[c] and val not in subgrids[grid_idx]:
                    rows[r].add(val)
                    cols[c].add(val)
                    subgrids[grid_idx].add(val)
                else:
                    return False

        return True
                
        