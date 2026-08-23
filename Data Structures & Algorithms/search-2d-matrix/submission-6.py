class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, COLS-1

        while r<ROWS and c>=0:
            mid = matrix[r][c]
            if target==mid:
                return True
            elif target>mid:
                r += 1
            else:
                c -= 1
        
        return False
        