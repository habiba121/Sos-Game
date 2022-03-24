# This code plays SOS game in which each player has to create the
# straight sequence S-O-S among connected squares (either diagonally, horizontally, or
# vertically), and to create as many such sequences as they can. If a player succeeds in creating
# an SOS, that player immediately takes another turn, and continues to do so until no SOS can
# be created on their turn. Otherwise turns alternate between players after each move.
# By Habiba Ahmed \ 20210120

board = [[' _ ', ' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ ', ' _ '],
         [' _ ', ' _ ', ' _ ', ' _ ']]


def display_board():
    for row in board:
        print(row)


def is_move_valid(row, col):
    if not row.isdigit() or not col.isdigit():  # Input is not a number
        return False
    elif int(row) > 3 or int(col) > 3:  # Invalid cell number
        return False
    elif not (board[int(row)][int(col)]).replace(" _ ", "0").isdigit():  # occupied cell
        return False
    else:  # Cell is good to choose
        return True


def get_move():
    while True:
        global row
        global col
        row = input("Choose a cell to tick, enter row (0 to 3): ")
        col = input("Choose a cell to tick, enter col (0 to 3): ")
        x = str(input("S or O: "))
        if not is_move_valid(row, col):
            print("Invalid Cell. Try again")
        else:
            board[int(row)][int(col)] = x
            row = int(row)
            col = int(col)
            break


def is_sos():
    global row
    global col
    row = int(row)
    col = int(col)
    if col - 2 >= 0:
        if [board[row][col], board[row][col - 1], board[row][col - 2]] == ['s', 'o', 's']:
            return True  # check if the cell and the two before it in the same row create st.sequence of SOS
    if col + 2 <= 3:
        if [board[row][col], board[row][col + 1], board[row][col + 2]] == ['s', 'o', 's']:
            return True  # check if the cell and the two after it in the same row create st.sequence of SOS
    if col - 1 >= 0 and col + 1 <= 3:
        if [board[row][col - 1], board[row][col], board[row][col + 1]] == ['s', 'o', 's']:
            return True  # check if the cell, the one after it and the one before in the same row
            # create st.sequence of SOS
    if row - 2 >= 0:
        if [board[row][col], board[row - 1][col], board[row - 2][col]] == ['s', 'o', 's']:
            return True  # check if the cell and the two before it in the same column create st.sequence of SOS
    if row + 2 <= 3:
        if [board[row][col], board[row + 1][col], board[row + 2][col]] == ['s', 'o', 's']:
            return True  # check if the cell and the two after it in the same column create st.sequence of SOS
    if row - 1 >= 0 and row + 1 <= 3:
        if [board[row - 1][col], board[row][col], board[row + 1][col]] == ['s', 'o', 's']:
            return True  # check if the cell, the one after it and the one before in the same column
            # create st.sequence of SOS
    if row + 2 <= 3 and col + 2 <= 3:
        if [board[row][col], board[row + 1][col + 1], board[row + 2][col + 2]] == ['s', 'o', 's']:
            return True  # check if the cell (at the top) and the two after it in the same diagonal
            # create st.sequence of SOS
    if row - 2 >= 0 and col + 2 <= 3:
        if [board[row][col], board[row - 1][col + 1], board[row - 2][col + 2]] == ['s', 'o', 's']:
            return True  # check if the cell (at the bottom) and the two after it in the same diagonal
            # create st.sequence of SOS
    if row - 2 >= 0 and col - 2 >= 0:
        if [board[row][col], board[row - 1][col - 1], board[row - 2][col - 2]] == ['s', 'o', 's']:
            return True  # check if the cell (at the bottom) and the two before it in the same diagonal
            # create st.sequence of SOS
    if row + 2 <= 3 and col - 2 >= 0:
        if [board[row][col], board[row + 1][col - 1], board[row + 2][col - 2]] == ['s', 'o', 's']:
            return True  # check if the cell (at the top) and the two before it in the same diagonal
            # create st.sequence of SOS
    if row - 1 >= 0 and row + 1 <= 3 and col - 1 >= 0 and col + 1 <= 3:
        if [board[row - 1][col + 1], board[row][col], board[row + 1][col - 1]] == ['s', 'o', 's']:
            return True  # check if the cell, the one before it and the one after in the same diagonal (right diagonal)
            # create st.sequence of SOS
    if row - 1 >= 0 and row + 1 <= 3 and col - 1 >= 0 and col + 1 <= 3:
        if [board[row - 1][col - 1], board[row][col], board[row + 1][col + 1]] == ['s', 'o', 's']:
            return True  # check if the cell, the one before it and the one after in the same diagonal (left diagonal)
            # create st.sequence of SOS


def play_game():
    points1 = 0
    points2 = 0
    num_moves = 0
    display_board()
    while num_moves < 16:  # while there are still empty cells
        print("Player1 Turn, points = ", points1)
        num_moves += 1
        get_move()
        display_board()
        sos = is_sos()
        while sos:
            num_moves += 1
            points1 += 1
            print("SOS!, Player1 has ", points1, " points.")
            get_move()
            display_board()
            sos = is_sos()
            if num_moves >= 16:
                break
        if num_moves >= 16:  # while the board is full
            if points1 > points2:
                print("Player1 Wins!")
                break
            elif points2 > points1:
                print("Player2 Wins!")
                break
            else:
                print("GAME OVER!!")
                break
        print("Player2 Turn, points = ", points2)
        num_moves += 1
        get_move()
        display_board()
        sos = is_sos()
        while sos:
            num_moves += 1
            points2 += 1
            print("SOS!, Player2 has ", points2, " points.")
            get_move()
            display_board()
            sos = is_sos()
            if num_moves >= 16:
                break
        if num_moves >= 16:  # while the board is full
            if points1 > points2:
                print("Player1 Wins!")
                break
            elif points2 > points1:
                print("Player2 Wins!")
                break
            else:
                print("GAME OVER!!")
                break


play_game()
