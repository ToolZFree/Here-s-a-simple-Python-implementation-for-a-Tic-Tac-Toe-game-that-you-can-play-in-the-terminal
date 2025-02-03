# Tic-Tac-Toe game

# Initialize the board
board = [' ' for _ in range(9)]  # A list of 9 empty spaces
current_winner = None  # Track the winner


# Display the board
def print_board():
    for i in range(0, 9, 3):
        print(f'{board[i]} | {board[i+1]} | {board[i+2]}')
        if i < 6:
            print('---------')


# Check for a win
def check_winner(player):
    global current_winner
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            current_winner = player
            return True
    return False


# Check if the board is full
def is_board_full():
    return ' ' not in board


# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    player = 'X'  # Player X starts first

    while True:
        try:
            # Get the player's move
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
            # Make the move
            board[move] = player
            print_board()
            
            # Check for a winner
            if check_winner(player):
                print(f"Player {player} wins!")
                break
            
            # Check for a tie
            if is_board_full():
                print("It's a tie!")
                break
            
            # Switch players
            player = 'O' if player == 'X' else 'X'
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# Start the game
play_game()
