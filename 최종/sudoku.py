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
