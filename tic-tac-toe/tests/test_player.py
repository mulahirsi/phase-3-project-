import unittest
from src.game.player import Player
from src.game.board import Board

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="Alice", symbol="X")
        self.board = Board()

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "Alice")
        self.assertEqual(self.player.symbol, "X")

    def test_make_move(self):
        self.player.make_move(self.board)
        self.assertEqual(self.board.board[0][0], "X")  # Assuming the player makes a move at position (0, 0)

    def test_make_move_invalid(self):
        self.board.update_board((0, 0), "X")  # Occupy the position
        with self.assertRaises(ValueError):
            self.player.make_move(self.board)  # Should raise an error since the position is already taken

if __name__ == '__main__':
    unittest.main()