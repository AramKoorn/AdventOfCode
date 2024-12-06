from collections import deque
from copy import deepcopy


grid = open("2024/day06/input.txt").read().splitlines()
print(grid)

for i, x in enumerate(grid):
    if "^" in x:
        start = (i, x.find('^'))
grid = [[x for x in l] for l in grid]

n = len(grid)
m = len(grid[0])

def new_dir(x, y):
    match (x, y):
        case (-1, 0): # up
            dx, dy = (0, 1)
        case (0, 1): # right
            dx, dy = (1, 0)
        case (1, 0):  # down
            dx, dy = (0, -1)
        case (0, -1): # left
            dx, dy = (-1, 0)
    return (dx, dy)



def is_loop(grid):
    visited = set()
    q = deque([(start, (-1, 0))])
    while True:
        # print(len(q))
        (x, y), (dx, dy) = q.popleft()
        i = x + dx
        j = y + dy

        if 0 <= x < n and 0 <= y and m and grid[x][y] != '#':
            if ((x, y), (dx, dy)) in visited:
                return True
            visited.add(((x, y), (dx, dy)))
        
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if  grid[i][j] != '#':
            q.append([(i, j), (dx, dy)])
        else:
            dx, dy = new_dir(dx, dy)
            q.append([(x, y), (dx, dy)])


t = 0
for i in range(n):
    for j in range(m):
        print(i, j)
        tmp = deepcopy(grid)
        tmp[start[0]][start[1]] = '.'
        if tmp[i][j] != "#" and (i, j) != (start):
            tmp[i][j] = "#"
            if is_loop(tmp):
                print(i, j)
                t += 1

print(t)
