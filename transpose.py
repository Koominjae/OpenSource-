def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed
