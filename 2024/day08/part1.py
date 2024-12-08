from collections import defaultdict
from itertools import combinations


grid = open("2024/day08/input.txt").read().splitlines()
cords = defaultdict(list)

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            cords[grid[i][j]].append((i, j))

def inside(x, y):
    return 0 <= x < n and 0 <= y < m


res = set()
def get_antinodes(p1, p2):
    # we create new ponts
    s = sorted((p1, p2))
    (x1, y1), (x2, y2) = s
    dx = abs(x2 - x1)
    dy = y2 - y1
    if y2 - y1 < 0:
        y1_new = y1 + abs(dy)
        y2_new = y2 - abs(dy)
    else:
        y1_new = y1 - abs(dy)
        y2_new = y2 + abs(dy)
    t1 = (x1 - abs(dx), y1_new)
    if inside(*t1):
        res.add(t1)
    t2 = (x2 + abs(dx), y2_new)
    if inside(*t2):
        res.add(t2)

for k, vals in cords.items():
    for p1, p2 in combinations(vals, 2):
        get_antinodes(p1, p2)

print(len(res))
# print(sorted(res    ))
