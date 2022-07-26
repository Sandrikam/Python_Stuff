#  TicTacToe Project

#   importing libraries
#   declaring variables

#   if game is still going

game_still_going = True

winner = None

currentPlayer = "X"
#   defining the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]  # spreading for visibility


#   display board

def disp_board():
    print(board[0] + "|" + board[1] + "|" + board[2])

    print(board[3] + "|" + board[4] + "|" + board[5])

    print(board[6] + "|" + board[7] + "|" + board[8])


#   handle turn

def handle_turn(player):
    position = input("choose position from 1-9: ")

    position = int(position) - 1

    board[position] = "X"

    disp_board()


def check_if_game_ovr():
    check_if_win()

    check_if_tie()


#   check tie

def check_if_tie():
    return


#   check win

def check_if_win():
    row_winner=check_rows()
    #   check columns
    column_winner=check_columns()
    #   check Diagonals
    diagonal_winner=check_diagonals()
    #   Check Rows
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return



def check_rows():
    global game_still_going
    #   checking same values
    row_1 = board[0] == board[1] == board[2] != "-"

    row_2 = board[3] == board[4] == board[5] != "-"

    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


#   check columns
def check_columns():
    global game_still_going
    #   checking same values
    col_1 = board[0] == board[3] == board[6] != "-"

    col_2 = board[1] == board[4] == board[7] != "-"

    col_3 = board[6] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[6]
    return


#   check Diagonals
def check_diagonals():
    global game_still_going
    #   checking same values
    diag_1 = board[0] == board[4] == board[8] != "-"

    diag_2 = board[6] == board[4] == board[2] != "-"

    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[1]
    return


#   flip Player

def flip_player():
    return


#   play game

def play_game():
    disp_board()

    while game_still_going:
        handle_turn(currentPlayer)

        check_if_game_ovr()

        flip_player()

    #   game ended.

    #   printing winner or whether it's a tie
    if winner == "X" or winner == "O":

        print(winner + ' is a winner')

    elif winner == None:

        print("Tie Bitch, Play Harder.")


play_game()