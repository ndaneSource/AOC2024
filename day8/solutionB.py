import re, math
f = open("./input.txt")

antennas = {}
antiNodes = []
maxRow = 0
maxCol = 0
for i, line in enumerate(f.readlines()):
    for col, char in enumerate(line.strip()):
        if char == "." or char == "#":
            continue
        if char in antennas:
            antennas[char].append([i,col])
        else:
            antennas[char] = [[i,col]]
    maxRow = i+1
    maxCol = len(line)
print(antennas)

def checkRepeat():
    print()

for i, points in enumerate(antennas.values()):
    while len(points) > 1:
        point = points.pop()
        for otherPoint in points:
            print(len(points))
            diffX = point[0] - otherPoint[0]
            diffY = point[1] - otherPoint[1]
            antiNode1 = []
            antiNode2 = []
            highPoints = []
            if diffX <=0 :
                antiNode1.append(otherPoint[0] + abs(diffX))
                antiNode2.append(point[0]-abs(diffX))
            else:
                antiNode1.append(otherPoint[0] - abs(diffX))
                antiNode2.append(point[0]+abs(diffX))
            if diffY <=0:
                antiNode1.append(otherPoint[1] + abs(diffY))
                antiNode2.append(point[1]-abs(diffY))
            else:
                antiNode1.append(otherPoint[1] - abs(diffY))
                antiNode2.append(point[1]+abs(diffY))
            
            if antiNode1[0] >=0 and antiNode1[0] < maxCol and antiNode1[1] >=0 and antiNode1[1] < maxRow:
                if str(antiNode1) not in antiNodes:
                    antiNodes.append(str(antiNode1))
            if antiNode2[0] >=0 and antiNode2[0] < maxCol and antiNode2[1] >=0 and antiNode2[1] < maxRow:
                if str(antiNode2) not in antiNodes:
                    antiNodes.append(str(antiNode2))
print(antiNodes)
print(len(antiNodes))


#6 , 8
#7 , 5
#-1,3

#5, 11
#8, 2