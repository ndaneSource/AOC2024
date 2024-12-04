import re
f = open("./test.txt")

grid = []
solution = 0
testForward = "XMAS"
testBackward = "SAMX"

for line in f.readlines():
    row = []
    for space in line:
        row.append(space)
    grid.append(row)

def testMatch(testString):
    matchCount = 0
    if testString == testForward:
        matchCount += 1
    if testString == testBackward:
        matchCount += 1
    return matchCount

def checkDir(row, col, rowInc, colInc):
    testString = ""
    for i in range(0,4):
        testString += grid[row][col]
        row += rowInc * 1
        col += colInc * 1
    print(testString)
    return testMatch(testString)

# def checkRight(row, col):
#     if col <= len(grid[0])-4:
#         testString = grid[row][col]+grid[row][col+1]+grid[row][col+2]+grid[row][col+3]
#         return testMatch(testString)
#     return 0
    
# def checkDown(row, col):
#     if row < len(grid)-3:
#         testString = grid[row][col]+grid[row+1][col]+grid[row+2][col]+grid[row+3][col]
#         return testMatch(testString)
#     return 0

# def checkDownRight(row, col):
#     # print(str(row)+", "+str(col))
#     if row < len(grid)-3 and col < len(grid[0])-4:
#         testString = grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]+grid[row+3][col+3]
#         return testMatch(testString)
#     return 0

# def checkDownLeft(row, col):
#     if row < len(grid)-3 and col >= 3:
#         testString = grid[row][col]+grid[row+1][col-1]+grid[row+2][col-2]+grid[row+3][col-3]
#         return testMatch(testString)
#     return 0


for row, line in enumerate(grid):
    for col, currentCharacter in enumerate(line):
        if currentCharacter == 'X' or currentCharacter == 'S':
            if col <= len(grid[0])-4:
                solution += checkDir(row, col, 0, 1)
            if row < len(grid)-3:
                solution += checkDir(row, col, 1, 0)
            if row < len(grid)-3 and col < len(grid[0])-4:
                solution += checkDir(row, col, 1, 1)
            if row < len(grid)-3 and col >= 3:
                solution += checkDir(row, col, 1, -1)

print(solution)
