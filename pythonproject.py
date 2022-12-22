N = 9


def isPossible(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startrow = row-row % 3
    startcol = col-col % 3

    for i in range(3):
        for j in range(3):
            if grid[i+startrow][j+startcol] == num:
                return False

    return True


def sudokoSolver(grid, row, col):
    if (row == N-1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if (grid[row][col] > 0):
        return sudokoSolver(grid, row, col+1)

    for num in range(1, N+1):
        if isPossible(grid, row, col, num):
            grid[row][col] = num

            if sudokoSolver(grid, row, col+1):
                return True

        grid[row][col] = 0
    return False


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print("\n\n\n")
print("────────────────────────────────────\n***********SUDOKO SOLVER**********\n────────────────────────────────────\n")

print("\n**********BEFORE SOLVING************")
print("\n")

print("────────────────────────────────────")


for i in range(N):
    if i % 3 == 0 and i != 0:
        print("────────────────────────────────────")
    for j in range(N):
        if j % 3 == 0 and j != 0:
            print(" | ", end="  ")
        if j == 8:
            print(grid[i][j])
        else:
            print(str(grid[i][j])+"  ", end="")
print("────────────────────────────────────\n")
print("\n")


print("***********AFTER SOLVING************")
print("\n")

print("────────────────────────────────────")


def print_board(bo):
    for i in range(len(bo)):

        if i % 3 == 0 and i != 0:
            print("────────────────────────────────────")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="  ")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+"  ", end="")


if sudokoSolver(grid, 0, 0):
    print_board(grid)
else:
    print("Invalid Solution")
print("────────────────────────────────────\n")
