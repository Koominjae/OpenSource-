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
