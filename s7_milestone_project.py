import random


def display_board(board):
    print('\n' * 100)
    print("Here is the current board: ")
    print(board[7:10])
    print(board[4:7])
    print(board[1:4])


def player_input():
    player1 = ''
    player2 = ''

    while player1 not in ['X', 'O']:

        player1 = input('Please pick a marker "X" or "O": ').upper()

        if player1 not in ['X', 'O']:
            print('Sorry, invalid choice!')

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    print(f"Ok, Player 1 is '{player1}' and Player 2 is '{player2}'")
    # return tuple - player 1marker, player 2 marker
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    if ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark)):
        return True
    else:
        return False
    pass


def choose_first():
    return random.randint(0, 1)


def space_check(board, position):
    return board[position] == ''


def full_board_check(board_to_check):
    if '' not in board_to_check:
        return True
    else:
        return False


def player_choice(board):
    choice = 0

    while choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, choice):

        choice = int(input('Pick a position (1 - 9): '))

        if choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print('Sorry, invalid choice!')

        if not space_check(board, int(choice)):
            print('Sorry, this position is taken, please try another position')
    return int(choice)


def replay():
    choice = ''

    while choice not in ['Y', 'N']:

        choice = input('Keep playing? (Y or N): ').upper()

        if choice not in ['Y', 'N']:
            print('Sorry, invalid choice!')

    if choice == 'Y':
        return True
    else:
        return False


def main():
    game_on = True
    print('Welcome to Tic Tac Toe!')

    while game_on:
        end_round = False

        # set the game
        board = [''] * 10
        display_board(board)

        # ask for user input and define player markers
        player1, player2 = player_input()

        # choose first player -
        player_marker = choose_first()

        if player_marker == 0:
            print('First will be Player 1')
        elif player_marker == 1:
            print('First will be Player 2')

        while not end_round:

            if player_marker == 0:
                print(f'Now it is Player 1 with marker "{player1}" turn')
                place_marker(board, player1, player_choice(board))
                display_board(board)
                player_marker = 1
                # check player 1 for win / lose
                if win_check(board, player1):
                    print(f'{player1} won!')
                    break
                else:
                    pass
            elif player_marker == 1:
                print(f'Now it is Player 2 with marker "{player2}" turn')
                place_marker(board, player2, player_choice(board))
                display_board(board)
                player_marker = 0
                # check player 2 for win / lose
                if win_check(board, player2):
                    print(f'{player2} won!')
                    break
                elif full_board_check(board):
                    print('Its a tie!')
                    end_round = True
                else:
                    pass

        # ask if players want continue game
        game_on = replay()


main()
