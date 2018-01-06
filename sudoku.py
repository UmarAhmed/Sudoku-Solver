#we will represent a sudoku grid with a list of lists
# the first list represents the first row and so forth
# any empty places are represented with a 0
# a sudoku puzzle is usually 9 x 9



# valid returns true if the current puzzle is in a valid state, and false otherwise
# we consider a state valid if there are no repeating elements in rows columns or squares
def valid(puzzle):
    map_row = [{} for _ in range(9)]
    map_col = [{} for _ in range(9)]
    map_cell = [[{} for _ in range(3)] for __ in range(3)]
    for i in range(9):
        for j in range(9):
            char = puzzle[i][j]
            if char == 0: continue
            if char in map_row[i]:
                return False
            else:
                map_row[i][char] = [i, j]
            if char in map_col[j]:
                return False
            else:
                map_col[j][char] = [i, j]
            if char in map_cell[i // 3][j // 3]:
                return False
            else:
                map_cell[i // 3][j // 3][char] = [i, j]
    return True

# solved returns true if the puzzle is solved and false otherwise
def solved(puzzle):
    blanks = sum([i.count(0) for i in puzzle])
    return blanks==0 and valid(puzzle)


def findNext(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def solveSudoku(grid, i=0, j=0):
    i, j = findNext(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True

            grid[i][j] = 0
    return False


def isValid(grid, i, j, e):
    if all([e != grid[i][x] for x in range(9)]) and all([e != grid[x][j] for x in range(9)]):
            mx, my = 3 * (i // 3), 3 * (j // 3)
            for x in range(mx, mx + 3):
                for y in range(my, my + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False

'''
testing = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
solveSudoku(testing) -> solves puzzle
print(testing) -> outputs solved puzzle
print(solved(testing)) -> True
'''