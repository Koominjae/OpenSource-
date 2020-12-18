def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,8)
        j = random.randint(0,8)
        if board[i][j] == 0:
            continue
        else:
            board[i][j] = 0
            no_of_holes -= 1
    return board
