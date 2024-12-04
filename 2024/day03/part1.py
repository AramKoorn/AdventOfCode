import re

f = open("2024/day03/input.txt", "r")
lines = [x.strip('\n') for x in f]
txt = "".join(lines)
print(txt)
# print(f.readlines())

# Regular expression pattern
pattern = r"mul\((-?\d+),(-?\d+)\)"

# Find all matches
matches = re.findall(pattern, txt)
t = 0
for a, b in matches:
    t += int(a) * int(b)

print(t)