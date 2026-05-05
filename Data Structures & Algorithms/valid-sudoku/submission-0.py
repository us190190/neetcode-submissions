class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):

                val = board[r][c]

                if val == '.':
                    continue
                elif (
                    val in rows[r] or
                    val in cols[c] or
                    val in box[(r//3,c//3)]
                ):
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    box[(r//3,c//3)].add(val)
        
        return True
                

            
        