class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        
    def display(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
                
    def make_move(self, position, symbol):
        if 0 <= position <= 8 and self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False
        
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]
                
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]
                
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
            
        return None
        
    def is_full(self):
        return " " not in self.board

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        
    def get_move(self):
        while True:
            try:
                position = int(input(f"{self.name}'s turn ({self.symbol}). Enter position (0-8): "))
                if 0 <= position <= 8:
                    return position
                print("Position must be between 0 and 8")
            except ValueError:
                print("Please enter a valid number")