def game_init():
	player1 = input("Type the name of player 1: ")
	player2 = input("Type the name of player 2: ")
	print(f"Welcome {player1} and {player2} to Connect Four. {player1} is playing with yellow and {player2} is playing with reds.")
	return player1, player2

def create_board():
	return [[" " for i in range(7)] for i in range(6)]

def print_board(board):
	for row in board:
		print(row)
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
	return False