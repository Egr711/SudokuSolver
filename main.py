#          0  1  2  3  4  5  6  7  8
sudoku = [[3, 4, 1, 2, 8, 7, 6, 9, 5],
          [7, 0, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 0, 0, 0, 0, 0, 0],
          [5, 0, 0, 0, 0, 0, 0, 0, 0],
          [9, 0, 0, 0, 0, 0, 0, 0, 0],
          [8, 0, 0, 0, 0, 0, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0],
          [6, 0, 0, 0, 0, 0, 0, 0, 0]]


def pickNumber(x, y):

    # Possible numbers
    nums = {0: False, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}
    # Current 9 square box
    currSquare = {"X": x // 3, "Y": y // 3}

    # Next two for loops eliminating numbers that would conflict
    for i in range(3):
        for j in range(3):
            currX = currSquare["X"] * 3 + i
            currY = currSquare["Y"] * 3 + j
            nums[sudoku[currY][currX]] = False

    for i in range(9):
        nums[sudoku[i][x]] = False
        nums[sudoku[y][i]] = False

    for key in nums:

        # If the number is possible
        if nums[key]:
            currX = x
            currY = y
            sudoku[currY][currX] = key

            # Finding next blank/0
            while currY < 9:
                currX = (currX + 1) % 9
                if currX == 0:
                    currY = (currY + 1)
                if currY == 9:
                    # Reached the end
                    return True
                if sudoku[currY][currX] == 0:
                    if pickNumber(currX, currY):
                        return True
                    break
    # No numbers fit, backtracking
    sudoku[y][x] = 0
    return False


x1 = 0
y1 = 0

while x1 < 9 and y1 < 9:
    if sudoku[y1][x1] == 0:
        if not pickNumber(x1, y1):
            print("No solution available")
        break
    x1 = (x1 + 1) % 9
    if x1 == 0:
        y1 = (y1 + 1)

for i in range(9):
    str1 = ""
    for j in range(9):
        str1 += str(sudoku[i][j]) + " "
    print(str1)
