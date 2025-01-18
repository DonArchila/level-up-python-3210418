# execute: python src/13%20Solve%20a%20Sudoku/my_sudoku.py
# Python program to solve a Sudoku puzzle

def is_valid(sudoku, row, col, num):
    for i in range(9):
      if sudoku[row][i] == num or sudoku[i][col] == num:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
      for j in range(3):
        if sudoku[start_row + i][start_col + j] == num:
          return False
    return True

def solve_sudoku(sudoku):
    for row in range(9):
      for col in range(9):
        if sudoku[row][col] == 0:
          for num in range(1, 10):
            if is_valid(sudoku, row, col, num):
              sudoku[row][col] = num
              if solve_sudoku(sudoku):
                return True
              sudoku[row][col] = 0
          return False
    return True

if __name__ == "__main__":
    sudoku = [
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

    if solve_sudoku(sudoku):
      for row in sudoku:
        print(row)
    else:
      print("No solution exists")