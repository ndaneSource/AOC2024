list1 = []
list2 = {}
f = open("./input.txt")

for line in f.readlines():
  #print(line)
  pairs = line.split("   ")
  #print(pairs)
  list1.append(int(pairs[0]))
  rightPair = int(pairs[1][0:-1])
  if list2.get(rightPair) is None:
    list2[rightPair] = 1
  else:
    list2[rightPair] +=1

list1.sort()

diff = 0
for position in range(0, len(list1)):
  number = list1[position]
  print(number, position)
  if list2.get(number) is None:
    continue
  diff += number * list2[number]

print(diff)
