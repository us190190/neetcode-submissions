class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, COLS-1

        while r<ROWS and c>-1:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r += 1
            else:
                c -= 1
        
        return False
        