from typing import List


class TicTacToe:
    def __init__(self, n):
        self._n = n

    def new_game(self):
        # self._board = [[None] * self._n for _ in range(self._n)]
        self._remaining_moves = self._n * self._n
        self._status = "Pending"
        self._player = 1  # 1 for player A, -1 for player B

        self._row_sums = [0] * self._n
        self._col_sums = [0] * self._n
        self._lr_diagonal_sum = 0
        self._rl_diagonal_sum = 0

        return self

    def move(self, i, j):
        if self._status != "Pending":
            return

        self._remaining_moves -= 1
        # self._board[i][j] = self._player

        self._update_sums(i, j)
        self._check_winner(i, j)

        self._player = -self._player

    def _update_sums(self, i, j):
        self._row_sums[i] += self._player
        self._col_sums[j] += self._player

        if i == j:
            self._lr_diagonal_sum += self._player

        if (i + j) == (self._n - 1):
            self._rl_diagonal_sum += self._player

    def _check_winner(self, i, j):
        if self._player * self._n in [
            self._row_sums[i],
            self._col_sums[j],
            self._lr_diagonal_sum,
            self._rl_diagonal_sum,
        ]:
            self._status = "A" if self._player == 1 else "B"

        elif self._remaining_moves == 0:
            self._status = "Draw"

    @property
    def status(self):
        return self._status


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        game = TicTacToe(3).new_game()
        for i, j in moves:
            game.move(i, j)
        return game.status
