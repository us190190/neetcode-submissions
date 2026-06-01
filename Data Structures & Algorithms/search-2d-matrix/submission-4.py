class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r, c = 0, len(matrix[0])-1

        while r<len(matrix) and c>-1:
            if target==matrix[r][c]:
                return True
            elif target>matrix[r][c]:
                r += 1
            else:
                c -= 1
        
        return False
        