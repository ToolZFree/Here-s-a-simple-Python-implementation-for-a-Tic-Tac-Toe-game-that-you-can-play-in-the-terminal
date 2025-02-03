import random

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


# Get a list of available moves
def get_available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']


# Minimax algorithm to find the best move
def minimax(depth, maximizing_player):
    available_moves = get_available_moves()
    
    # If the game is over, return the score
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_board_full():
        return 0

    if maximizing_player:
        best_score = -float('inf')
        for move in available_moves:
            board[move] = 'O'  # Try computer's move
            score = minimax(depth + 1, False)
            board[move] = ' '  # Undo the move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in available_moves:
            board[move] = 'X'  # Try player's move
            score = minimax(depth + 1, True)
            board[move] = ' '  # Undo the move
            best_score = min(score, best_score)
        return best_score


# Get the best move for the computer (AI)
def get_computer_move():
    available_moves = get_available_moves()
    best_score = -float('inf')
    best_move = None

    for move in available_moves:
        board[move] = 'O'  # Try computer's move
        score = minimax(0, False)
        board[move] = ' '  # Undo the move

        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move


# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    player = 'X'  # Player X starts first

    while True:
        if player == 'X':
            # Player's turn
            try:
                move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
                # Make the move
                board[move] = player
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
        else:
            # Computer's turn
            print("Computer's turn:")
            move = get_computer_move()
            board[move] = player

        # Print the board after every move
        print_board()
        
        # Check for a winner
        if check_winner(player):
            if player == 'X':
                print("Player X wins!")
            else:
                print("Computer wins!")
            break
        
        # Check for a tie
        if is_board_full():
            print("It's a tie!")
            break
        
        # Switch players
        player = 'O' if player == 'X' else 'X'


# Start the game
play_game()
