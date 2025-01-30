def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col]:
            return False  # Check column

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False  # Check left diagonal

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False  # Check right diagonal

    return True


def solve_n_queens_util(board, row, N):
    if row == N:
        return True  # Base case: all queens placed

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = 0  # Backtrack

    return False


def print_board(board, N):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if solve_n_queens_util(board, 0, N):
        print_board(board, N)
    else:
        print("No solution exists")


if __name__ == "__main__":
    N = int(input("Enter N for N-Queens: "))
    solve_n_queens(N)