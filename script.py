from functions import create_board, game_init, print_board, add_token, check_winner

if __name__ == '__main__':
    player1, player2 = game_init()
    turn = 0
    board = create_board()
    while True:
        print_board(board)
        if not check_winner(board):
            if turn == 0:
                while turn == 0:
                    try:
                        print(f"Its {player1} turn with 'Y'!")
                        pos = input(f"{player1}, select where you want to drop you token (From 1 to 7): ")
                        board = add_token("Y", board, int(pos))
                        turn = 1
                    except ValueError as e:
                        print(e)
            elif turn == 1:
                while turn == 1:
                    try:
                        print(f"Its {player2} turn with 'R'!")
                        pos = input(f"{player2}, select where you want to drop you token (From 1 to 7): ")
                        board = add_token("R", board, int(pos))
                        turn = 0
                    except ValueError as e:
                        print(e)
        else:
            if turn:
                print(f"The winner is {player1}")
                break
            else:
                print(f"The winner is {player2}")
                break