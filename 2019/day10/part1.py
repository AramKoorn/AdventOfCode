import math
from collections import Counter


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
        mx = max(mx, len(c))
    
print(mx)
