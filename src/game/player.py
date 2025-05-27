class Player:
    """A class representing a Tic Tac Toe player"""
    
    def __init__(self, name, symbol):
        """
        Initialize a new player
        
        Args:
            name (str): Player's name
            symbol (str): Player's symbol (X or O)
        """
        self.name = name
        self.symbol = symbol
        self.wins = 0
        
    def get_move(self):
        """
        Get the player's move
        
        Returns:
            int: Position on board (0-8)
        """
        while True:
            try:
                position = int(input(f"{self.name}'s turn ({self.symbol}). Enter position (0-8): "))
                if 0 <= position <= 8:
                    return position
                print("Position must be between 0 and 8")
            except ValueError:
                print("Please enter a valid number")
                
    def increment_wins(self):
        """Increment player's win count"""
        self.wins += 1
        
    def get_stats(self):
        """
        Get player's statistics
        
        Returns:
            str: Player's name, symbol and wins
        """
        return f"Player: {self.name} ({self.symbol}) - Wins: {self.wins}"