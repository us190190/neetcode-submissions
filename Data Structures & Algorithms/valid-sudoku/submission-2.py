class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols, cells = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                cell = str(row//3)+"_"+str(col//3)
                if val == ".":
                    continue
                elif (val not in rows[row]) and (val not in cols[col]) and (val not in cells[cell]):
                    rows[row].add(val)
                    cols[col].add(val)
                    cells[cell].add(val)
                    continue
                else:
                    return False
        
        return True
        