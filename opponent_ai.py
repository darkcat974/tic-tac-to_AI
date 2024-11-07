# ai.py

import math

# Function to check for a winner
def check_winner(player, board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner("O", board):
        return 1
    if check_winner("X", board):
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Get the best move for the AI
def get_ai_move(board, ai_player):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = ai_player
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move
