# game`s name
print("X--Tic Tac Toe--O")
# creating the playing 'field' board

board = ['*', '*', '*',
         '*', '*', '*',
         '*', '*', '*']

#             Global  Variables

# Is the game going on?
is_game_going = True

# show the winner
winner = None

# showing who is currently playing
playing = 'X'


# showing the game board

def display_board():
    print('[' + board[0] + '][' + board[1] + '][' + board[2] + ']')
    print('[' + board[3] + '][' + board[4] + '][' + board[5] + ']')
    print('[' + board[6] + '][' + board[7] + '][' + board[8] + ']')


# This function contains all functions in one
# Starts the game by executing the board for the player

def play_game():

    # board calling
    display_board()

    while is_game_going:

        # current player action
        handle_turn(playing)

        # check if game overed
        is_game_over()

        # changing the player
        change_player()
    # condition for 'game over' result calling

    if winner == '(X)' or winner == '(O)':
        print(f'won -- {winner}')
    elif winner:
        print('Tie')


# choosing the position on the board by player`s input

def handle_turn(player):
    print(player + "'s turn")
    position = input('Choose any cell on the board from 1 to 9: ')

# 1 Checking the available positions
# 2 and if the player`s input is correct?

    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4',
                               '5', '6', '7', '8', '9']:
            position = input('Choose any cell on the board from 1 to 9: ')

    # getting the index in board(list)
        position = int(position) - 1

    # is the 'cell' position available on the board?
        if board[position] == '*':
            valid = True
        else:
            print('X_O, try one more time.')

    #
    board[position] = player

    # calling the playing board
    display_board()


#              "CHECKing" function block

# here we are checking conditions for win or tie

def is_game_over():

    # [1] win
    if_win()

    # [2] tie
    if_tie()


# [1] 'winner checking' functions in all possible
# positions 'combinations' in the board

def if_win():

    # global variable
    global winner

    # rows 1
    rows_winner = if_rows()

    # columns 2
    columns_winner = if_columns()

    # diagonals 3
    diagonals_winner = if_diagonals()

    # Victory if:
    if rows_winner:
        winner = rows_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None


# 1 rows checking
def if_rows():
    # global variable
    global is_game_going

    # Check if any of the rows have all the same value
    # and is not empty
    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"

    #
    if row_1 or row_2 or row_3:
        is_game_going = False

    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    # Or return None if there was no winner
    else:
        return None


# 2 columns checking
def if_columns():

    # global variable
    global is_game_going

    # Check if any of the columns have all the same value
    # and is not empty
    column_1 = board[0] == board[3] == board[6] != "*"
    column_2 = board[1] == board[4] == board[7] != "*"
    column_3 = board[2] == board[5] == board[8] != "*"

    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        is_game_going = False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    # Or return None if there was no winner
    else:
        return None


# 3 diagonals checking
def if_diagonals():

    # global variable
    global is_game_going

    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "*"
    diagonal_2 = board[2] == board[4] == board[6] != "*"

    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        is_game_going = False

    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    # Or return None if there was no winner
    else:
        return None


# [2] tie checking functions in all possible positions

def if_tie():

    # global variable
    global is_game_going

    # If board is full
    if "*" not in board:
        is_game_going = False
        return True

    # Else there is no tie
    else:
        return False

#              EXIT FROM "CHECKing" function block


# changing the player
def change_player():

    # global variable
    global playing

    # If the current player was X, make it O
    if playing == "X":
        playing = "O"

    # Or if the current player was O, make it X
    elif playing == "O":
        playing = "X"


# Starts the game by executing the board for the player
play_game()
