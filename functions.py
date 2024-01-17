def game_init():
    print("Welcome to connect four. The objective of this game is align four tokes of you color. The number you select is where you will drop the token.")
    player1 = input("Type the name of player 1: ")
    player2 = input("Type the name of player 2: ")
    print(f"Welcome {player1} and {player2} to Connect Four. {player1} is playing with yellow and {player2} is playing with reds.")
    return player1, player2

def create_board():
	return [[" " for i in range(7)] for i in range(6)]

def print_board(board):
    for row in board:
        print(row)
        print(" ")
    print([str(i) for i in range(1, 8)])    

def add_token(token, board, pos):
	if pos > 7 or pos < 1:
		raise ValueError
	
	i = -1
	pos -= 1
	
	if board[0][pos].strip():
		print("This row is full")
		raise ValueError
	
	while True:
		if not board[i][pos].strip():
			board[i][pos] = token
			break
		else:
			i -= 1
		
	return board
	
def check_winner(board):
    # Check for rows
    for row in board:
        for i in range(4):
            if row[i] == "Y" and row[i+1] == "Y" and row[i+2] == "Y" and row[i+3] == "Y":
                return True
            elif row[i] == "R" and row[i+1] == "R" and row[i+2] == "R" and row[i+3] == "R":
                return True
	    
    # Check for columns
    for i in range(3):
        for j in range(7):
            if board[i][j] == "Y" and board[i+1][j] == "Y" and board[i+2][j] == "Y" and board[i+3][j] == "Y":
                return True
            elif board[i][j] == "R" and board[i+1][j] == "R" and board[i+2][j] == "R" and board[i+3][j] == "R":
                return True
            
    # Check for diagonals (\)
    for i in range(3):
        for j in range(4):
            if board[i][j] == "Y" and board[i+1][j+1] == "Y" and board[i+2][j+2] == "Y" and board[i+3][j+3] == "Y":
                  return True
            if board[i][j] == "R" and board[i+1][j+1] == "R" and board[i+2][j+2] == "R" and board[i+3][j+3] == "R":
                  return True
            
    # Check for diagonals (/)
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == "Y" and board[i+1][j-1] == "Y" and board[i+2][j-2] == "Y" and board[i+3][j-3] == "Y":
                  return True
            if board[i][j] == "R" and board[i+1][j-1] == "R" and board[i+2][j-2] == "R" and board[i+3][j-3] == "R":
                  return True

    else:
        return False