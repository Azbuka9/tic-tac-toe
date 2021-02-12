# ---------- Global Variables --------

# Game bord
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# if game is still going
game_still_going = True

# Who won_or_tie?
winner = None

# Who's turn is it
current_player = "X"


# Display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input('Chose a position from 1-9: ')

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Chose a position from 1-9: ')

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print('You cant go there, Go again')

    board[position] = player
    display_board()


def check_rows():
    # set up global variables
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set up global variables
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_still_going
    dialog_1 = board[0] == board[4] == board[8] != '-'
    dialog_2 = board[6] == board[4] == board[2] != '-'
    if dialog_1 or dialog_2:
        game_still_going = False
    if dialog_1:
        return board[0]
    elif dialog_2:
        return board[6]
    return


def check_for_winner():
    # Set up global variables
    global winner

    # check_rows()
    row_winner = check_rows()

    # check_columns()
    column_winner = check_rows()

    # check_diagonals()
    diagonal_winner = check_diagonals()

    if row_winner:
        # There was a win
        winner = row_winner
    elif column_winner:
        # There was a win
        winner = column_winner
    elif diagonal_winner:
        # There was a win
        winner = diagonal_winner
    else:
        # There was no win
        winner = None
    return


def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# play game of tic-tac-toe
def play_game():
    # display initial board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " won.")
    elif winner is None:
        print('Tie.')


play_game()
