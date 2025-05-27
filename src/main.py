from game.board import Board
from game.player import Player
from utils.helpers import display_game_history

def main():
    # Initialize game components
    board = Board()
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    current_player = player1
    
    # Welcome message
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 0-8 as shown below:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    
    # Main game loop
    while True:
        # Display current board state
        print("\nCurrent board:")
        board.display()
        
        # Get player move
        while True:
            position = current_player.get_move()
            if board.make_move(position, current_player.symbol):
                break
            print("That position is already taken!")
        
        # Check for winner
        winner = board.check_winner()
        if winner:
            print("\nFinal board:")
            board.display()
            print(f"\nCongratulations! {current_player.name} wins!")
            current_player.increment_wins()
            break
            
        # Check for draw
        if board.is_full():
            print("\nFinal board:")
            board.display()
            print("\nIt's a draw!")
            break
            
        # Switch players
        current_player = player2 if current_player == player1 else player1

    # Display game history
    display_game_history()
    
    # Ask to play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        return

if __name__ == "__main__":
    main()