from game.board import Board
from game.player import Player
from utils.helpers import display_game_history

def play_game(player1, player2):
    """Run a single game between two players"""
    board = Board()
    current_player = player1

    while True:
        print("\nCurrent board:")
        board.display()
        
        # Get player move or handle commands
        while True:
            move = input(f"{current_player.name}'s turn ({current_player.symbol}). Enter position (0-8), 'q' to quit, or 'r' to restart: ")
            
            # Handle quit command
            if move.lower() == 'q':
                print("\nThanks for playing!")
                return False, None
                
            # Handle restart command
            if move.lower() == 'r':
                print("\nRestarting game...")
                return True, None
                
            # Handle regular move
            try:
                position = int(move)
                if 0 <= position <= 8 and board.make_move(position, current_player.symbol):
                    break
                print("Invalid move! Position already taken or out of range.")
            except ValueError:
                print("Please enter a number between 0-8, 'q' to quit, or 'r' to restart")

        # Check for winner
        winner = board.check_winner()
        if winner:
            print("\nFinal board:")
            board.display()
            print(f"\nCongratulations! {current_player.name} wins!")
            current_player.increment_wins()
            return True, current_player

        # Check for draw
        if board.is_full():
            print("\nFinal board:")
            board.display()
            print("\nIt's a draw!")
            return True, None

        # Switch players
        current_player = player2 if current_player == player1 else player1

def main():
    """Main game loop"""
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 0-8 as shown below:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")

    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")

    while True:
        continue_game, winner = play_game(player1, player2)
        
        if not continue_game:
            break
            
        display_game_history()
        
        if winner:
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                print("\nThanks for playing!")
                break

if __name__ == "__main__":
    main()