import time

board = [
    [0,0,6,0,0,1,0,0,7],
    [0,0,9,0,8,0,0,5,0],
    [0,0,2,3,4,0,0,0,0],
    [0,0,0,0,5,7,0,0,1],
    [0,5,0,0,0,0,0,8,0],
    [9,0,0,1,3,0,0,0,0],
    [0,0,0,0,1,3,9,0,0],
    [0,9,0,0,6,0,7,0,0],
    [3,0,0,5,0,0,4,0,0]
]

#find empty fill on the board
def find_empty(board):
    # row position
    for r in range(len(board)):
        # col position
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return (r, c)
    return None

# find valid guess
def valid_guess(board, row, col):
    val_guess = list(range(1,10))
    board_num = []
    row_num = board[row]
    col_num = []
    for y in range(len(board)):
        col_num.append(board[y][col])
    # check 3x3
    row_start = (row // 3) * 3 # 2//3=0 4//3=1 7//3=2
    col_start = (col // 3) * 3
    cube_num = []
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            cube_num.append(board[r][c])
    #A set is an unordered collection of items. Every set element is unique (no duplicates)
    board_num = list(set(row_num + col_num + cube_num)) # convert set back to list
    board_num.pop(0) # remove 1st int which happens to be 0 , sudoku only has 1 - 9
    val_guess = list(set(val_guess) - set(board_num))
    return val_guess

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find 
    for i in (valid_guess(board, row, col)):
        board[row][col] = i
        if solve_sudoku(board):
            return True
        board[row][col] = 0 
    return False

def print_board(bo):
    for r in range(len(bo)):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - - ")
        for c in range(len(bo[0])):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")
            if c == 8:
                print(bo[r][c])
            else:
                print(str(bo[r][c]) + " ", end="")


tic = time.perf_counter()
print_board(board)
solve_sudoku(board)
print("______________________________________")
print_board(board)
toc = time.perf_counter()
print(f"jon {toc - tic:0.4f} seconds")
