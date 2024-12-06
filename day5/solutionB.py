import re, math
f = open("./input.txt")

rules = {}
addingRules = True
solution = 0

def movePageInSequence(sequence, wrongPosition, afterPosition, wrongPage):
    sequence.insert(afterPosition+1, wrongPage)
    sequence.pop(wrongPosition)
    #print(sequence)
    return sequence
    
def correctSequenceOrder(rules, sequence, wrongPosition):
    wrongPage = sequence[wrongPosition]
    #print(str(sequence)+" "+str(wrongPage))
    for i in range(len(sequence)-1, wrongPosition, -1):
        #print(str(i)+" "+str(sequence[i]))
        if sequence[i] in rules and wrongPage in rules[sequence[i]]:
            return movePageInSequence(sequence, wrongPosition, i, wrongPage)

def getMiddlePage(sequence):
    middle = math.floor((len(sequence)-1) /2)
    print(str(sequence)+" middle:"+str(middle)+" is "+str(sequence[middle]))
    return int(sequence[middle])
    
def checkPageOrder(rules, sequence):
    for i in range(1, len(sequence)):
        page1 = sequence[i-1]
        page2 = sequence[i]
        if page1 in rules and page2 in rules[page1]:
            continue
        else:
            return i-1
    return -1

for line in f.readlines():
    if not line.strip():
        addingRules = False
        continue
    
    if addingRules:
        pair = line.strip().split("|")
        if pair[0] not in rules:
            rules[pair[0]] = [pair[1]]
        else:
            rules[pair[0]].append(pair[1])
    else:
        sequence = line.strip().split(",")
        wrongPosition = checkPageOrder(rules, sequence)
        if wrongPosition >= 0:
            while(wrongPosition >=0):
                sequence = correctSequenceOrder(rules, sequence, wrongPosition)
                wrongPosition = checkPageOrder(rules, sequence)
            solution+= getMiddlePage(sequence)
print(solution)