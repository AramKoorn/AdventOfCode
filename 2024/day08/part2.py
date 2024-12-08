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

    while inside(x1, y1):
        res.add((x1, y1))
        x1 = x1 - abs(dx)
        if y2 - y1 < 0:
            y1 = y1 + abs(dy)
        else:
            y1 = y1 - abs(dy)
        
    while inside(x2, y2):
        res.add((x2, y2))
        x2 = x2 + abs(dx)
        if y2 - y1 < 0:
            y2 = y2 - abs(dy)
        else:
            y2 = y2 + abs(dy)

for k, vals in cords.items():
    for p1, p2 in combinations(vals, 2):
        get_antinodes(p1, p2)

print(len(res))
# print(sorted(res    ))
