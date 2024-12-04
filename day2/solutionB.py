
list1 = []
list2 = {}
f = open("./input.txt")

def alteredLevels(levels, position):
    if position == 0:
        return levels[1:]
    elif position == len(levels)-1:
        return levels[0:-1]
    else:
        return levels[0:position]+ levels[position+1:]

def testSafe(levels, increment, tolerence):
    for i in range(0, len(levels)-1):
        difference = (int(levels[i]) - int(levels[i+1])) * increment
        if difference < 1 or difference > 3:
           # print(levels[i]+ " "+ levels[i+1]+" dif:"+str(difference))
            if tolerence == 0:
                return 0
            else:
                safe = testSafe(alteredLevels(levels, i+1), increment, 0)
                safe += testSafe(alteredLevels(levels, i), increment, 0)
                safe += testSafe(alteredLevels(levels, i-1), increment, 0)
                if safe > 0:
                    print("safe "+str(safe))
                    return 1
                else: 
                    return 0
    print(levels)
    return 1

safeLevel = 0
for line in f.readlines():
    levels = line.split()
    isIncreasing = int(levels[0])-int(levels[1]) < 0
    safeLevel += testSafe(levels, -1, 1)
    safeLevel += testSafe(levels, 1, 1)
print(safeLevel)

