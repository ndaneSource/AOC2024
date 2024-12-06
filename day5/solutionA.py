import re, math
f = open("./input.txt")

rules = {}
orders = False
solution = 0

def checkOrder(rules, sequence):
    for i in range(1, len(sequence)):
        page1 = sequence[i-1]
        page2 = sequence[i]
        if page1 in rules and page2 in rules[page1]:
            continue
        else:
            return 0
    middle = math.floor((len(sequence)-1) /2)
    print(str(sequence)+" "+str(middle)+" "+str(sequence[middle]))
    return int(sequence[middle])



for line in f.readlines():
    if not line.strip():
        orders = True
        continue
    
    if not orders:
        pair = line.strip().split("|")
        if pair[0] not in rules:
            rules[pair[0]] = [pair[1]]
        else:
            rules[pair[0]].append(pair[1])
    else:
        sequence = line.strip().split(",")
        solution += checkOrder(rules, sequence)

print(solution)