def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # empty cell
                for num in range(1, 10):  # try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # recursive call
                            return True
                        board[row][col] = 0  # backtrack
                return False
    return True  # If the board is completely filled, return True

# Example Sudoku puzzle (0 denotes empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    for row in board:
        print(" ,".join(str(num) if num != 0 else ' ' for num in row))

print("Sudoku board before solving:")
print_board(sudoku_board)
    
print("\n")
if solve_sudoku(sudoku_board):
    # for row in sudoku_board:
    #     print(row)
    print_board(sudoku_board)
    
else:
    print("No solution exists")