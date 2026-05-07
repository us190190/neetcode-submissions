class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]

                idx = str(r//3) + "_" + str(c//3)

                if val == ".":
                    continue
                elif (
                    val in rows[r] or
                    val in cols[c] or
                    val in sqrs[idx]
                ):
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    sqrs[idx].add(val)
        
        return True
        