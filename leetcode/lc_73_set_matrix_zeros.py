from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_count = len(matrix)
        col_count = len(matrix[0])

        fill_first_row = any(matrix[0][j] == 0 for j in range(col_count))
        fill_first_col = any(matrix[i][0] == 0 for i in range(row_count))

        # Mark for filling, record result in the first row and col
        for i in range(1, row_count):
            for j in range(1, col_count):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Fill with 0
        for i in range(1, row_count):
            for j in range(1, col_count):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if fill_first_row:
            for j in range(col_count):
                matrix[0][j] = 0

        if fill_first_col:
            for i in range(row_count):
                matrix[i][0] = 0
