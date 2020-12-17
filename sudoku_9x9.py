import random

def initialize_board_9x9():
    row1 = [1,2,3,4,5,6,7,8,9]
    random.shuffle(row1)
    row2 = row1[3:6] + row1[6:9] + row1[0:3]
    row3 = row2[3:6] + row2[6:9] + row2[0:3]
    row4 = [row1[1], row1[2], row1[0], row1[4], row1[5], row1[3], row1[7], row1[8], row1[6]]
    row5 = row4[3:6] + row4[6:9] + row4[0:3]
    row6 = row5[3:6] + row5[6:9] + row5[0:3]
    row7 = [row4[1], row4[2], row4[0], row4[4], row4[5], row4[3], row4[7], row4[8], row4[6]]
    row8 = row7[3:6] + row7[6:9] + row7[0:3]
    row9 = row8[3:6] + row8[6:9] + row8[0:3]
    return [row1, row2, row3, row4, row5, row6, row7, row8, row9]

def shuffle_ribbons(board):
    top = board[:3]
    middle = board[3:6]
    bottom = board[6:9]
    random.shuffle(top)
    random.shuffle(middle)
    random.shuffle(bottom)
    return top + middle + bottom

def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

def create_solution_board_9x9():
    board = initialize_board_9x9()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone

def get_level():
    level = input("난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요. : ")
    while level not in ("1","2","3"):
        level = input("난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요. : ")
    if level == "1":
        return 30
    elif level == "2":
        return 41
    else:
        return 50

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

def get_integer(message, i ,j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudoku():
    solution_board = create_solution_board_9x9()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0 :
        i = get_integer("가로줄번호(1~9) : ", 1,9) - 1
        j = get_integer("세로줄번호(1~9) : ", 1,9) - 1
        if puzzle_board[i][j] != 0 :
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~9) : ", 1,9)
        if n == solution_board[i][j] :
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else :
            print(n, "가(이) 아닙니다. 다시 해보세요. ")
    print("잘 하셨습니다. 또 들려주세요.")
