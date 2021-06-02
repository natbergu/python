puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
def sudoprint(sudoku):
    print("┌─────────┬─────────┬─────────┐")
    for row in sudoku:
        if sudoku.index(row) == 3 or sudoku.index(row) == 6:
            print("├─────────┼─────────┼─────────┤")
        output = str(row).replace("[", "").replace("]", "").replace(", ", "  ").replace("0", " ")
        out0 = output[:7]
        out1 = output[9:16]
        out2 = output[18:]
        print("│ " + out0 + " │ " + out1 + " │ " + out2 + " │")
    print("└─────────┴─────────┴─────────┘")
print("puzzle:")
sudoprint(puzzle)
def solve(sudoku):
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                for number in range(1, 10):
                    candidate = True
                    for place in range(9):
                        if sudoku[row][place] == number:
                            candidate = False
                    for place in range(9):
                        if sudoku[place][column] == number:
                            candidate = False
                    rorigin = 3 * (row // 3)
                    corigin = 3 * (column // 3)
                    for roffset in range(3):
                        for coffset in range(3):
                            if sudoku[rorigin + roffset][corigin + coffset] == number:
                                candidate = False
                    if candidate:
                        sudoku[row][column] = number
                        solve(sudoku)
                        sudoku[row][column] = 0
                return
    print("solution:")
    sudoprint(sudoku)
    input("check for more solutions?")
solve(puzzle)
