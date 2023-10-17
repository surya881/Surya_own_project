import random

# Function to create the game board
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to display the game board
def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

# Function for a player's turn
def player_turn(board, player):
    print(f"\n{player}'s turn:")
    
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        
        if row in range(3) and col in range(3) and board[row][col] == ' ':
            board[row][col] = player
            break
        else:
            print("Invalid move. Please try again.")

# Function for the computer's turn
def computer_turn(board, computer):
    print("\nComputer's turn:")
    
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if board[row][col] == ' ':
            board[row][col] = computer
            break

# Main game function
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2/Computer: O")
    
    player1 = 'X'
    player2 = 'O'
    
    board = create_board()
    display_board(board)
    
    while True:
        # Player 1's turn
        player_turn(board, player1)
        display_board(board)
        
        if check_winner(board, player1):
            print("Player 1 wins!")
            break
        
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Player 2's/Computer's turn
        if player2 == 'O':
            player_turn(board, player2)
        else:
            computer_turn(board, player2)
        
        display_board(board)
        
        if check_winner(board, player2):
            if player2 == 'O':
                print("Player 2 wins!")
            else:
                print("Computer wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

# Main program
if __name__ == "__main__":
    play_game()