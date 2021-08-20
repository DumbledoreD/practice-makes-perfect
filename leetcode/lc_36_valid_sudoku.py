from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self._validate_rows(board)
            and self._validate_cols(board)
            and self._validate_box(board)
        )

    def _validate_rows(self, board):
        for row in board:
            count = defaultdict(int)

            for i in row:
                if i != "." and count[i]:
                    return False

                count[i] += 1

        return True

    def _validate_cols(self, board):
        for j in range(9):
            count = defaultdict(int)

            for i in range(9):
                if board[i][j] != "." and count[board[i][j]]:
                    return False

                count[board[i][j]] += 1

        return True

    def _validate_box(self, board):
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                count = defaultdict(int)

                for c in range(9):
                    i, j = divmod(c, 3)
                    i += row_offset
                    j += col_offset

                    if board[i][j] != "." and count[board[i][j]]:
                        return False

                    count[board[i][j]] += 1

        return True
