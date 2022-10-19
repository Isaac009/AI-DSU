# boardSize is the size of the 2D matrix   boardSize*boardSize
boardSize = 9

def print_board(board):
    print("=======================")
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -  ")

        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == (boardSize-1):
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")
    print("=======================")

def isValidMove(board, row, col, num):
    for i in range(boardSize):
        if board[i][col] == num:
            return False
    
    for j in range(boardSize):
        if board[row][j] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def SudokuSolver(board, row, col):
    if (row == boardSize - 1 and col == boardSize):
        return True

    if col == boardSize:
        row += 1
        col = 0
    if board[row][col] > 0:
        return SudokuSolver(board, row, col + 1)
    for num in range(1, boardSize + 1, 1):
        if isValidMove(board, row, col, num):
            board[row][col] = num
            if SudokuSolver(board, row, col + 1):
                return True

        board[row][col] = 0
    return False

# 0 = Empty cell
board = [[0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3, 4, 6, 2, 0],
        [6, 0, 3, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 4, 8, 3, 5, 0, 7],
        [0, 0, 0, 0, 5, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 9, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 1],
        [8, 0, 0, 5, 4, 7, 3, 9, 6],
        [0, 0, 0, 0, 2, 1, 0, 0, 0]]
 
if (SudokuSolver(board, 0, 0)):
    print_board(board)
else:
    print("There is no existing valid solution.")

