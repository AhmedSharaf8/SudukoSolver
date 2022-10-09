from traceback import print_tb


def find_next_empty(puzzle):
    # find the next row, col that's not filled = -1
    # return None, None if there is no empty spots 
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None


def is_valid(puzzle, guess, row, col):
    # return true if the guess is valid

    # check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # check the col
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False

    # check the 3 x 3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def solve_sudoku(puzzle):
    # choose a spot to make a guess
    row, col = find_next_empty(puzzle)

    # if there is no spots left
    if row is None:
        return True

    # if there is a spot make a guess between 1 and 9
    for guess in range(1, 10):  # guess a number between 1 and 9
        # check if this is valid 
        if is_valid(puzzle, guess, row, col):
            # place the guess in the spot
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1

    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)