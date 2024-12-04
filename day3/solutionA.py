import re
f = open("./input.txt")
input = f.read()

result = 0

m = re.findall("mul\(\d*,\d*\)", input)
print(m)
for match in m:
    pair = re.findall("\d+", match)
    print(pair)
    result += int(pair.pop()) * int(pair.pop())

print(result)