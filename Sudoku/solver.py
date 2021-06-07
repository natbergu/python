class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def sudoprint(self):
        print("┌─────────┬─────────┬─────────┐")
        for row in self.sudoku:
            if self.sudoku.index(row) == 3 or self.sudoku.index(row) == 6:
                print("├─────────┼─────────┼─────────┤")
            output = str(row).replace("[", "").replace("]", "").replace(", ", "  ").replace("0", " ")
            out0 = output[:7]
            out1 = output[9:16]
            out2 = output[18:]
            print("│ " + out0 + " │ " + out1 + " │ " + out2 + " │")
        print("└─────────┴─────────┴─────────┘")

    def solve(self):
        for row in range(9):
            for column in range(9):
                if self.sudoku[row][column] == 0:
                    for number in range(1, 10):
                        candidate = True
                        for place in range(9):
                            if self.sudoku[row][place] == number or self.sudoku[place][column] == number:
                                candidate = False
                        rorigin = 3 * (row // 3)
                        corigin = 3 * (column // 3)
                        for roffset in range(3):
                            for coffset in range(3):
                                if self.sudoku[rorigin + roffset][corigin + coffset] == number:
                                    candidate = False
                        if candidate:
                            self.sudoku[row][column] = number
                            self.solve()
                            self.sudoku[row][column] = 0
                    return
        print("solution:")
        self.sudoprint()
        print("raw:")
        print(self.sudoku)
        if str(input("check for more solutions? > ")) in {"n", "N", "no", "No", "nO", "NO"}:
            print("alright...")
            return

## puzzle = Sudoku([[0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
##                  [0, 0, 0, 0, 0, 0, 0, 0, 0]])

puzzle = Sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]])

print("puzzle:")
puzzle.sudoprint()
puzzle.solve()
