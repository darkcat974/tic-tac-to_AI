# main.py
from opponent_ai import get_ai_move  # Import the AI's move function
from player_ai import get_player_move  # Import the player's move function
from sys import argv # Import the argv module

# Initialize the game board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check for a winner
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

# Check for a tie
def check_tie():
    return " " not in board

# Main game loop
def game_loop(mode="player"):
    # Player plays as "X"
    current_player = "X"
    while True:
        print_board()
        # AI play as "O"
        if current_player == "O":
            if mode == "versus":
                move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            else:
                # Send the board to Get the AI's move
                move = get_ai_move(board, "O")
                print(f"AI chooses position {move + 1}")
        else:
            if mode == "ai":
                # Send the board to Get the AI's move
                move = get_player_move(board, "X")
                print(f"AI chooses position {move + 1}")
            else:
                move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1

        #check move
        if board[move] == " ":
            board[move] = current_player
            #check win condition
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return
            #change player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Position already taken. Try again.")
        # Check for a tie
        if check_tie():
            print_board()
            print("It's a tie!")
            return

def usage():
    print("Usage: python main.py [s|p|v]")
    print("\t-s (spectator): AI vs AI")
    print("\t-p (solo player): Player vs AI")
    print("\t-v (player versus player): Player vs Player")
    return

def main():
    if len(argv) != 2:
        usage()
    if len(argv) > 1 and argv[1] == "v":
        return game_loop("versus")
    if len(argv) > 1 and argv[1] == "p":
        return game_loop("player")
    if len(argv) > 1 and argv[1] == "s":
        return game_loop("ai")
    else:
        usage()
        return

if __name__ == "__main__":
    main()
