import unittest
from unittest.mock import patch
from src.game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player", "X")

    def test_player_initialization(self):
        """Test player initialization with correct attributes"""
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.symbol, "X")
        self.assertEqual(self.player.wins, 0)

    @patch('builtins.input', return_value='4')
    def test_valid_move(self, mock_input):
        """Test player makes a valid move"""
        self.assertEqual(self.player.get_move(), 4)

    @patch('builtins.input', side_effect=['9', 'abc', '4'])
    def test_invalid_moves(self, mock_input):
        """Test handling of invalid moves"""
        self.assertEqual(self.player.get_move(), 4)

    def test_increment_wins(self):
        """Test win counter incrementation"""
        initial_wins = self.player.wins
        self.player.increment_wins()
        self.assertEqual(self.player.wins, initial_wins + 1)

    def test_get_stats(self):
        """Test player statistics display"""
        expected = "Player: Test Player (X) - Wins: 0"
        self.assertEqual(self.player.get_stats(), expected)

if __name__ == '__main__':
    unittest.main()