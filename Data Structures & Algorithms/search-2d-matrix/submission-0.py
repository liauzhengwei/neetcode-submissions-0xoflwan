class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = m - 1

        while i<n and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target <= matrix[i][j]:
                j -= 1
            else:
                i += 1

        return False