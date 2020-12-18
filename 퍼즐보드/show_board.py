def show_board(board):
    print('S |', 1, 2, 3, 4, 5, 6, 7, 8, 9)
    print('- |  -  -  -  -  -  -  -  -  -')
    i = 1
    for row in board:
        print(i, end=' | ')
        for entry in row:
            if entry == 0:
                print('.', end='  ')
            else:
                print(entry, end=' ')
        print()
        i += 1
