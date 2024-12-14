import re
from functools import reduce


f = open("2024/day14/input.txt").read().splitlines()
r = 103 
c = 101
# r = 7
# c = 11

pattern = r'([-+]?\d+),([-+]?\d+)'
pos = []

steps = 100

for l in f:
    x, y, dx, dy = 2, 4, 2, -3
    matches = re.findall(pattern, l)
    (x, y), (dx, dy) = matches   
    x, y, dx, dy, = int(x), int(y), int(dx), int(dy)
    nc = (steps * dx + x) % c
    nr = (steps * dy + y) % r
    pos.append((nr, nc))


q1 = [(x, y) for (x, y) in pos if x < r // 2 and y < c // 2]
q2 = [(x, y) for (x, y) in pos if x < r // 2 and y > c // 2]
q3 = [(x, y) for (x, y) in pos if x > r // 2 and y < c // 2]
q4 = [(x, y) for (x, y) in pos if x > r // 2 and y > c // 2]


l = [len(q) for q in [q1, q2, q3, q4]]
result = reduce(lambda x, y: x * y, l)
print(result)

print(pos)