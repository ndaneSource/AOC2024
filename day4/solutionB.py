import re
f = open("./input.txt")

grid = []
solution = 0
testForward = "MAS"
testBackward = "SAM"

for line in f.readlines():
    row = []
    for space in line:
        row.append(space)
    grid.append(row)

def checkRight(row, col):
    ret = 0
    if col <= len(grid[0])-3 and col > 0 and row > 0 and row <= len(grid)-2:
        test1 = grid[row-1][col-1]+grid[row][col]+grid[row+1][col+1]
        test2 = grid[row+1][col-1]+grid[row][col]+grid[row-1][col+1]
        print(str(row)+", "+ str(col)+" "+ test1 + " " + test2)
        if test1 == testForward or test1 == testBackward:
            if test2 == testForward or test2 == testBackward:
                print("yes f")
                return 1
    return ret


for row in range(0,len(grid)):
    for col in range(0,len(grid[row])):
        currentCharacter = grid[row][col]
        if currentCharacter == 'A':
            solution += checkRight(row, col)

print(solution)
