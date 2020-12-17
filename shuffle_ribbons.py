def shuffle_ribbons(board):
    top = board[:3]
    middle = board[3:6]
    bottom = board[6:9]
    random.shuffle(top)
    random.shuffle(middle)
    random.shuffle(bottom)
    return top + middle + bottom
