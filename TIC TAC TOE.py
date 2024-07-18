# 1. Create the Tic Tac Toe board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# 2. Display the board to the players
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# 3. Allow two players to take turns marking X and O on the board
def get_player_input(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column, e.g., 1 1): ")
        row, col = map(int, move.split())
        row -= 1  # Adjusting index to be zero-based
        col -= 1  # Adjusting index to be zero-based
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            return row, col
        else:
            print("Invalid move. The cell is already occupied or out of bounds. Try again.")

# 4. Check for a win or a tie after each move
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# 5. Display the result and ask if the players want to play again
def play_game():
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        row, col = get_player_input(board, current_player)
        board[row][col] = current_player
        
        if check_winner(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            display_board(board)
            print("The game is a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        play_game()

play_game()
