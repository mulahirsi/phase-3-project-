import unittest
from src.game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_empty(self):
        self.assertEqual(self.board.board, [" " for _ in range(9)])

    def test_make_valid_move(self):
        self.assertTrue(self.board.make_move(0, "X"))
        self.assertEqual(self.board.board[0], "X")

    def test_make_invalid_move(self):
        self.board.make_move(0, "X")
        self.assertFalse(self.board.make_move(0, "O"))

    def test_check_winner_row(self):
        self.board.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertEqual(self.board.check_winner(), "X")

    def test_check_winner_column(self):
        self.board.board = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
        self.assertEqual(self.board.check_winner(), "O")

    def test_check_winner_diagonal(self):
        self.board.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertEqual(self.board.check_winner(), "X")

    def test_board_is_full(self):
        self.board.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        self.assertTrue(self.board.is_full())