from collections import deque


grid = open("2024/day06/input.txt").read().splitlines()
print(grid)

for i, x in enumerate(grid):
    if "^" in x:
        start = (i, x.find('^'))

# print(grid)
print(start)
n = len(grid)
m = len(grid[0])

visited = set()
visited.add(start)
q = deque([(start, (-1, 0))])

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



while True:
    # print(len(q))
    (x, y), (dx, dy) = q.popleft()
    print(dx, dy)
    i = x + dx
    j = y + dy

    if 0 <= x < n and 0 <= y and m and grid[x][y] != '#':
        visited.add((x, y))
    if i < 0 or i >= n or j < 0 or j >= m:
        print(len(visited))
        break
    if  grid[i][j] != '#':
        q.append([(i, j), (dx, dy)])
    else:
        print("test")
        dx, dy = new_dir(dx, dy)
        q.append([(x, y), (dx, dy)])
