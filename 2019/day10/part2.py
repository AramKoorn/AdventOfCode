import math
from collections import Counter, defaultdict


grid = open("2019/day10/input.txt").read().splitlines()

n = len(grid)
m = len(grid[0])

ast = set()

for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            ast.add((i, j))

c = Counter()
mx = 0

for a in ast:
    c = Counter()
    for i, j in ast:
        dx = a[0] - i
        dy = a[1] - j
        angle = math.atan2(dx, dy)
        c[angle] += 1
    
    if max(mx, len(c)) > mx:
        ms = a
    mx = max(mx, len(c))


def get_angle(r, c):
    dr = ms[0] - r
    dc = ms[1] - c
    angle = math.atan2(dc, dr)
    degrees = math.degrees(angle)
    norm =  (degrees + 360) % 360
    norms = abs(norm - 360)
    return 0 if norms == 360 else norms
    

angles = defaultdict(list)
for r, c in ast:
    dist = abs(r - ms[0]) + abs(c + ms[1])
    angle = get_angle(r, c)
    angles[angle].append((dist, r, c))

all_angles = sorted(list(angles))
i = 0

for _ in range(200):
    popped = True
    while popped:
        key = all_angles[i % len(all_angles)]
        if angles[key]:
            angles[key].sort()
            val = angles[key].pop(0)
            popped = False
        i += 1

print(val[2] * 100 + val[1])