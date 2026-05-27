class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r,c = 0, len(matrix[0])-1

        while r<len(matrix) and c>=0:
            cell = matrix[r][c]
            if target==cell:
                return True
            elif target<cell:
                c -= 1
            else:
                r += 1
        
        return False
        