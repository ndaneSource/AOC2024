import re, math
f = open("./test.txt")

grid = []
steps = {}
guardPosition =[]
guardDirection = 0
loops = []
obsticles = {}
directionOrder = [[-1,0],[0,1],[1,0],[0,-1]]

for line in f.readlines():
    row = []
    for i, space in enumerate(line):
        if space == "^":
            guardPosition = [len(grid), i]
        row.append(space)
    grid.append(row)

def outsideBounds(nextSpace):
    if nextSpace[0] >= len(grid)-1 or nextSpace[0] < 0:
        return True
    if nextSpace[1] >= len(grid[0])-1 or nextSpace[1] < 0:
        return True
    return False

def turnGuard(guardDirection):
    guardDirection += 1
    if guardDirection == 4:
        guardDirection = 0
    return guardDirection

def guardLookLeft(guardDirection):
    guardDirection -= 1
    if guardDirection == -1:
        guardDirection = 3
    return guardDirection

def getSpace(location, direction):
    space = [location[0]+directionOrder[direction][0],location[1]+directionOrder[direction][1]]
    if outsideBounds(space):
        return -1
    return space


def addObsticle(guardDirection, grid):
    lookLeft = guardLookLeft(guardDirection)
    leftSpace = getSpace(guardPosition, lookLeft)
    if leftSpace == -1:
        return
    
    if grid[leftSpace] == "#":
        if str(leftSpace) in obsticles:
            obsticles[str(leftSpace)].append(guardDirection)
        else:
            obsticles[str(leftSpace)]=[guardDirection]

    
while True:
    nextSpace = [guardPosition[0]+directionOrder[guardDirection][0],guardPosition[1]+directionOrder[guardDirection][1]]
    if grid[nextSpace[0]][nextSpace[1]] == "#":
        guardDirection = turnGuard(guardDirection)
        continue
    if outsideBounds(nextSpace):
        print("breaking")
        break
    guardPosition = nextSpace
    print(guardPosition)
    if str(guardPosition) not in steps:
        steps[str(guardPosition)] = guardDirection
    

print(len(steps))
print(guardPosition)
print(len(loops))