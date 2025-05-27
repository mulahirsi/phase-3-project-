from utils.db import Database

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
        self.db = Database()
        self.id = self._get_or_create_player()
        
    def _get_or_create_player(self):
        """Get existing player or create new one in database"""
        cursor = self.db.conn.cursor()
        cursor.execute(
            "SELECT id, wins FROM players WHERE name = ? AND symbol = ?",
            (self.name, self.symbol)
        )
        result = cursor.fetchone()
        
        if result:
            self.id, self.wins = result
            return self.id
            
        cursor.execute(
            "INSERT INTO players (name, symbol, wins) VALUES (?, ?, ?)",
            (self.name, self.symbol, self.wins)
        )
        self.db.conn.commit()
        return cursor.lastrowid

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
        """Increment player's win count and update database"""
        self.wins += 1
        cursor = self.db.conn.cursor()
        cursor.execute(
            "UPDATE players SET wins = wins + 1 WHERE id = ?",
            (self.id,)
        )
        cursor.execute(
            "INSERT INTO games (winner_id) VALUES (?)",
            (self.id,)
        )
        self.db.conn.commit()
        
    def get_stats(self):
        """
        Get player's statistics from database
        
        Returns:
            str: Player's name, symbol and wins
        """
        cursor = self.db.conn.cursor()
        cursor.execute(
            "SELECT wins FROM players WHERE id = ?",
            (self.id,)
        )
        self.wins = cursor.fetchone()[0]
        return f"Player: {self.name} ({self.symbol}) - Wins: {self.wins}"