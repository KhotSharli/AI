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

# Function to get the computer's move using a basic winning strategy
def get_computer_move(board):
    magic_square = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    available_moves = [i for i in range(9) if board[i] == EMPTY]

    # Check if player can win in the next move and block them
    for move in available_moves:
        board[move] = X  # Assume player's move
        if check_winner(board) == X:
            board[move] = EMPTY
            return move
        board[move] = EMPTY

    # Choose the best defensive move based on the Magic Square values
    best_move = -1
    best_value = float('inf')  # Start with a high value for defensive prioritization

    for move in available_moves:
        board[move] = O  # Assume computer's move
        if check_winner(board) == O:
            board[move] = EMPTY
            return move
        board[move] = EMPTY

        # Evaluate moves based on Magic Square values (choose the lowest value for defense)
        if magic_square[move] < best_value:
            best_value = magic_square[move]
            best_move = move

    # If no immediate winning or blocking move, play the best defensive move based on Magic Square
    return best_move

# Function to check if there is a winner or if it's a draw
def check_winner(board):
    for combination in WINNING_COMBINATIONS:
        if all(board[block] == X for block in combination):
            return X
        elif all(board[block] == O for block in combination):
            return O
    # If no winner, check for draw
    if all(board[i] != EMPTY for i in range(9)):
        return 'Draw'
    return None  # Game still in progress

# Function to print the current state of the board
def print_board(board):
    print(f"{board[0]}  {board[1]}  {board[2]}")
    print(f"{board[3]}  {board[4]}  {board[5]}")
    print(f"{board[6]}  {board[7]}  {board[8]}")

if __name__ == "__main__":
    main()