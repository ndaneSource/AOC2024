import re
f = open("./input.txt")
input = f.read()

result = 0
reg = re.compile(r"((?:mul\(\d+,\d+\))|(?:do\(\))|(?:don't\(\)))")
m = reg.findall(input)
print(m)
enabled = True
for match in m:
    if match == "don't()":
        enabled = False
        continue
    if match == "do()":
        enabled = True
        continue
    if enabled:
        print(match)
        pair = re.findall("\d+", match)
        print(pair)
        result += int(pair.pop()) * int(pair.pop())

print(result)