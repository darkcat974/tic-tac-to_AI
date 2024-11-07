import random

# Define the possible winning conditions (rows, columns, diagonals)
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]             # diagonals
]

def check_winner(board, player):
    # Check if the player has won on the board
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def get_empty_positions(board):
    # Return a list of empty positions on the board.
    return [i for i, spot in enumerate(board) if spot == " "]

def get_ai_move(board, ai_player):
    # Get the AI's best move based on a heuristic approach.
    opponent = "X" if ai_player == "O" else "O"

    # Check if AI can win in the next move
    for move in get_empty_positions(board):
        board[move] = ai_player
        if check_winner(board, ai_player):
            return move
        board[move] = " "  # Undo the move

    # Block the opponent's winning move
    for move in get_empty_positions(board):
        board[move] = opponent
        if check_winner(board, opponent):
            board[move] = " "  # Undo the move
            return move
        board[move] = " "  # Undo the move

    # Otherwise, pick a random available move
    return random.choice(get_empty_positions(board))
