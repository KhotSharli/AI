# Constants for player symbols
EMPTY = '-'
X = 'X'
O = 'O'

# Define winning combinations
WINNING_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Main function to play the game
def main():
    board = [EMPTY] * 9  # Initialize the board
    current_player = X  # X always starts
    winner = None

    while winner is None:
        print_board(board)
        if current_player == X:
            move = get_player_move(board)
            board[move] = X
        else:
            move = get_computer_move(board)
            board[move] = O
        winner = check_winner(board)
        if winner:
            break
        current_player = O if current_player == X else X  # Switch players

    print_board(board)
    if winner == X:
        print("X wins!")
    elif winner == O:
        print("O wins!")
    else:
        print("It's a draw!")

# Function to get the player's move from the console
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == EMPTY:
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the computer's move using Minimax algorithm
def get_computer_move(board):
    _, best_move = minimax(board, O)
    return best_move

def minimax(board, player):
    # Base cases: check if the game is over
    winner = check_winner(board)
    if winner == O:
        return 1, None  # If 'O' wins, return a positive score
    elif winner == X:
        return -1, None  # If 'X' wins, return a negative score
    elif winner == 'Draw':
        return 0, None  # If it's a draw, return a neutral score

    # Initialize variables for best score and move
    best_score = float('-inf') if player == O else float('inf')
    best_move = None

    # Iterate through all possible moves
    for move in range(9):
        if board[move] == EMPTY:
            # Try the move
            board[move] = player
            # Recursively call minimax to evaluate the move
            score, _ = minimax(board, X if player == O else O)
            # Undo the move
            board[move] = EMPTY

            # Update best score and move based on player
            if player == O:
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move

    return best_score, best_move

# Function to check if there is a winner or if it's a draw
def check_winner(board):
    for combination in WINNING_COMBINATIONS:
        if all(board[block] == X for block in combination):
            return X
        elif all(board[block] == O for block in combination):
            return O
    if all(board[i] != EMPTY for i in range(9)):
        return 'Draw'
    return None

# Function to print the current state of the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

if __name__ == "__main__":
    main()