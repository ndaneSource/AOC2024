
list1 = []
list2 = {}
f = open("./input.txt")

def testSafe(levels, increment):
    for i in range(0, len(levels)-1):
        difference = (int(levels[i]) - int(levels[i+1])) * increment
        if difference < 1 or difference > 3:
            print(levels[i]+ " "+ levels[i+1]+" dif:"+str(difference))
            return 0
    return 1

safeLevel = 0
for line in f.readlines():
    levels = line.split()
    isIncreasing = int(levels[0])-int(levels[1]) < 0
    if isIncreasing:
        safeLevel += testSafe(levels, -1)
    else:
        safeLevel += testSafe(levels, 1)
print(safeLevel)

