import json

print("hello world")

list1 = []
list2 = []
f = open("./input.txt")

for line in f.readlines():
  #print(line)
  pairs = line.split("   ")
  #print(pairs)
  list1.append(int(pairs[0]))
  list2.append(int(pairs[1][0:-1]))

list1.sort()
list2.sort()

diff = 0
for position in range(0, len(list1)):
  diff += abs(list1[position] - list2[position])

print(diff)
