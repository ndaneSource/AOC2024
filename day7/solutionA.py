import re, math
f = open("./input.txt")

solution = 0

def checkValid(lineSolution, progress, parts, position):
    if position == len(parts):
        return progress == lineSolution

    part = int(parts[position])
    sumSolution = progress + part
    productSolution = progress * part


    # if sumSolution > lineSolution:
    #     sSol = False
    # else:
    sSol = checkValid(lineSolution, sumSolution, parts, position+1)
    
    # if productSolution > lineSolution:
    #     pSol = False
    # else:
    pSol = checkValid(lineSolution, productSolution, parts, position+1)

    return pSol or sSol

for line in f.readlines():
    lineSolution, partsStr = line.strip().split(":")
    parts = partsStr.strip().split(' ')
    #print(lineSolution)
    result = checkValid(int(lineSolution), int(parts[0]), parts, 1)
    if result:
        #print(lineSolution)
        solution += int(lineSolution)
        #print(solution)
    else:
        print("not "+lineSolution)
        print(solution)

print(solution)

#wrong 303876485678
